"""Model functions sensitivity analysis clinic at CSDMS 2019.

Written by Nathan Lyons, May 2019
"""
from os.path import join

from landlab import RasterModelGrid
from landlab.components import FastscapeEroder, FlowAccumulator, LinearDiffuser
from landlab.io import write_esri_ascii
import numpy as np

import experiment_funcs as ef


def calculate_factor_values(levels):
    """Calculate values of trial factors.

    Parameters
    ----------
    levels : dictionary
        The factor levels of the trial.

    Returns
    -------
    dictionary
        Calculated factor values.
    """
    # Set parameters based on factor levels.
    f = {
            'U': 10**levels['U_exp'],
            'K': 10**levels['K_exp'],
            'D': 10**levels['D_exp'],
            'base_level_fall': 10**levels['base_level_fall']}

    return f


def run_model(f, output_path):
    """Run a trial of the base level fall model.

    Parameters
    ----------
    f : dictionary
        Model trial factors.
    output_path : string
        Path where outputs will be saved.
    """
    # Set parameters.
    nrows = 200
    ncols = 100
    dx = 100
    dt = 1000

    # Create initial topography with random elevation values.
    mg = RasterModelGrid(nrows, ncols, dx)
    z = mg.add_zeros('node', 'topographic__elevation')
    np.random.seed(1)
    z += np.random.rand(z.size)
    mg.set_closed_boundaries_at_grid_edges(right_is_closed=True,
                                           top_is_closed=False,
                                           left_is_closed=True,
                                           bottom_is_closed=False)

    # Instantiate model components.
    fa = FlowAccumulator(mg, flow_director='D8')
    sp = FastscapeEroder(mg, K_sp=f['K'], m_sp=0.5, n_sp=1)
    ld = LinearDiffuser(mg, linear_diffusivity=f['D'], deposit=False)

    # Set variables to evaluate presence of steady state.
    initial_conditions_set = False
    at_steady_state = False
    relief_record = []
    recent_mean = []
    recent_std = []
    step = 0

    # Set number of time steps, `steps_ss` that is the time window to evaluate
    # steady state.
    steps_ss = 1000

    # Create a dictionary to store responses.
    response = {}

    # Run model until steady state is reached.

    uplift_per_step = f['U'] * dt
    core_mask = mg.node_is_core()

    print('Running model until elevation reaches steady state.')

    while not at_steady_state:
        fa.run_one_step()
        sp.run_one_step(dt)
        ld.run_one_step(dt)
        z[core_mask] += uplift_per_step

        at_steady_state = check_steady_state(step * dt, z, step, steps_ss,
                                             relief_record, recent_mean,
                                             recent_std)

        if at_steady_state and not initial_conditions_set:
            initial_conditions_set = True

            # Save elevation of the initial conditions.
            fn = join(output_path, 'initial_conditions_elevation.asc')
            write_esri_ascii(fn, mg, ['topographic__elevation'], clobber=True)

            # Retain steady state relief, `relief_ss`.
            z_core = z[mg.core_nodes]
            relief_ss = z_core.max() - z_core.min()
            response['relief_at_steady_state'] = relief_ss

            # Find steady state divide position.
            divide_y_coord_initial = get_divide_position(mg)

            # Perturb elevation.
            base_level_nodes = mg.y_of_node == 0
            z[base_level_nodes] -= f['base_level_fall']
            at_steady_state = False

        elif at_steady_state and initial_conditions_set:
            response['time_back_to_steady_state'] = step * dt

            # Get divide migration distance.
            divide_y_coord_final = get_divide_position(mg)
            d = divide_y_coord_final - divide_y_coord_initial
            response['divide_migration_distance'] = d

            # Save final elevation.
            fn = join(output_path, 'final_elevation.asc')
            write_esri_ascii(fn, mg, ['topographic__elevation'], clobber=True)

        # Advance step counter.
        step += 1

    # Write response to file.

    path_r = join(output_path, 'response.csv')
    ef.write_data(response, path_r)


def check_steady_state(time, z, step, step_win, relief_record, recent_mean,
                       recent_std):
    relief_record.append(z.max() - z.min())

    if step < step_win:
        # If fewer than `step_win` time steps have occurred, calculate the
        # running mean and standard deviation the entire elapsed time period.
        recent_mean.append(np.mean(relief_record))
        recent_std.append(np.std(relief_record))

    else:
        # If more than `step_win` time steps have occurred, calculate the
        # running mean and standard deviation over the most recent `step_win`
        # time steps.
        recent_mean.append(np.mean(relief_record[-step_win:]))
        recent_std.append(np.std(relief_record[-step_win:]))

        mean_pct_change = (np.abs(recent_mean[-1] - recent_mean[-step_win]) /
                           np.abs(recent_mean[-1] + recent_mean[-step_win]))
        std_pct_change = (np.abs(recent_std[-1] - recent_std[-step_win]) /
                          np.abs(recent_std[-1] + recent_std[-step_win]))

        # If the percent change is less than 1% for both the mean and
        # standard deviation, flag the system as at steady state.
        thresh = 0.01
        minor_mean_change = mean_pct_change < thresh
        minor_std_change = std_pct_change < thresh or recent_std[-1] == 0
        at_steady_state = minor_mean_change and minor_std_change

        if step % 1e3 == 0 or at_steady_state:
            print('ss_check:', 'time', time, 'mean_pct_change',
                  mean_pct_change, 'std_pct_change', std_pct_change)

        return at_steady_state


def get_divide_position(grid):
    z = grid.at_node['topographic__elevation'].reshape(grid.shape)
    z_row_mean = z.mean(axis=1)
    divide_y_coord = z_row_mean.argmax() * grid.dy
    return divide_y_coord
