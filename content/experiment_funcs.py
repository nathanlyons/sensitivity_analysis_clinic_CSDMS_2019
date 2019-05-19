"""Sensitivity analysis funcs for sensitivity analysis clinic at CSDMS 2019.

Written by Nathan Lyons, May 2019
"""
from csv import DictWriter
from os import listdir
from os.path import isfile, join

import numpy as np
from pandas import concat, read_csv


def get_problem_dict():
    # Get the path of the file with the bounds of factors.

    file_name = 'factor_bounds.csv'
    design_path = join('..', 'experiment_design', file_name)

    # Create a problem dictionary with the keys required by SALib.

    df = read_csv(design_path)

    problem = {'names': df.names.values.tolist()}
    problem['num_vars'] = len(problem['names'])
    bounds_min = df.bounds_min.values
    bounds_max = df.bounds_max.values
    problem['bounds'] = np.column_stack((bounds_min, bounds_max))

    return problem


def get_path_dict():
    path = {'factor_levels_file': join('..', 'experiment_design',
                                       'trial_factor_levels.txt'),
            'trials': join('..', 'model_output', 'trials')}

    return path


def get_compilated_response(trials_path):
    df_list = []

    for trial_path in listdir(trials_path):
        if trial_path == '.DS_Store':
            continue

        trial_id = int(trial_path.split('.')[1])
        response_path = join(trials_path, trial_path, 'response.csv')

        if not isfile(response_path):
            continue

        df = read_csv(response_path)
        df['trial_id'] = trial_id
        df_list.append(df)

    compilated_response = concat(df_list, ignore_index=True, sort=True)
    compilated_response.to_csv()

    return compilated_response


def write_data(response, full_path):
    """Write model data to csv.
    """
    with open(full_path, 'w') as f:
        w = DictWriter(f, response.keys())
        w.writeheader()
        w.writerow(response)
