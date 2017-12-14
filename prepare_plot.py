import matplotlib.pyplot as plt
import numpy as np

def prepare_plot(xticks, yticks, figsize = (10.5, 6), hide_labels = False, grid_color = '#999999',
                grid_width = 1.0):
    """Template for generating the plot layout"""
    plt.close()
    fig, ax = plt.subplots(figsize = figsize, facecolor = 'white', edegecolor = 'white')
    ax.axes_tick_params(labelcolor = '#999999', labelsize = '10')
    for axis, ticks in [(ax.get_xaxis(),xticks), (ax.get_yaxis(), yticks)]:
        axis.set_ticks_position('none')
        axis.set_ticks(ticks)
        axis.label.set_color('#999999')
        if hide_labels: axis.set_ticklabels([])

    plt.grid(color = grid_color, linewidth = grid_width, linestyle = '-')
    map(lambda position: ax.spines[position].set_visible(False), ['bottom','top','left','right'])
    return fig, ax
