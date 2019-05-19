import matplotlib.pyplot as plt
import numpy as np


def plot_sobol_indices(Si, problem, title=None, factor_names=None):

    # Get indices.

    factors = problem['names']
    s1 = Si['S1']
    s1_conf = Si['S1_conf']
    st = Si['ST']
    st_conf = Si['ST_conf']

    # Set up plot.

    fig, ax = plt.subplots(nrows=1, ncols=1)
    
    x_shift = 0.08
    x_vals_1 = np.arange(0 - x_shift, len(s1) - x_shift, 1)
    x_vals_2 = np.arange(0 + x_shift, len(st) + x_shift, 1)

    # Plot indices.

    ax.errorbar(x_vals_1, s1, yerr=s1_conf, marker='o', markersize=9,
        linewidth=0.8, linestyle='None', color='k', capsize=0,
        label='first order', markerfacecolor='w', markeredgewidth=0.8)
    ax.errorbar(x_vals_2, st, yerr=st_conf, marker='s', markersize=9,
        linewidth=0.8, linestyle='None', color='k', capsize=0,
        label='total order', markeredgewidth=0.8)

    if title != None:
        ax.set_title(title)

    ax.legend(handletextpad=0.001)

    # Set x axis.

    if factor_names == None:
        xlabels = factors
    else:
        xlabels = factor_names
    
    ax.set_xticks(range(len(factors)))
    ax.set_xticklabels(xlabels)
    ax.set_xlabel('factors')

    # Set y axis.

    ax.set_ylim([-0.1, 1.1])
    ax.set_yticks(np.linspace(0, 1, 3))
    ax.set_yticks([0.25, 0.75], minor=True)
    plt.setp(ax.get_yminorticklabels(), visible=False)
    ax.set_ylabel('Sobol index')

    # Set horizontal lines.

    for y in np.linspace(0, 1,5):
        ax.axhline(y=y, linestyle=':', color='0.8', linewidth=0.5)

    plt.tight_layout()
