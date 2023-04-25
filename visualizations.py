"""
# -- ------------------------------------------------------------------------------------------------------------------------ -- #   
# -- project: MonteCarlo-Simulations                                                                                             -- #           
# -- script: visualizations.py : Python script with visualizations functionalities                                            -- #                 
# -- author: EstebanMqz                                                                                                       -- #  
# -- license: CC BY 3.0                                                                                                       -- #
# -- repository: https://github.com/EstebanMqz/MonteCarlo-Simulations/blob/main/visualizations.py                                -- #           
# -- ------------------------------------------------------------------------------------------------------------------------ -- #  
"""

from os import path
#Dependencies
import functions as fn
import data as dt
import main
#Libraries in vs
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=UserWarning)


def MC_plot(simulations, E_V, xlabel , ylabel, i_capital, f_capital):
    """Plots a line plot of events for n Monte Carlo simulations.
    Parameters
    ----------
    simulation : pandas.DataFrame
        Dataframe of Monte Carlo simulations.
    E_V : pandas.DataFrame
        The expected value of the simulation.
    xlabel : str
        The label of the x-axis.
    ylabel : str
        The label of the y-axis.
    i_capital : int
        The initial value of the variable to be simulated.
    f_capital : int
        The final value of the variable simulated.

    Returns
    -------
    line_plot : matplotlib.pyplot
        Plot of events time-series for N MonteCarlo simulations.
    """

    #If ROI is negative make the color red, otherwise green.
    ROI = round((E_V.iloc[-1][0] / E_V.iloc[0][0]) - 1, 6)
    color = ["red" if ROI < 0 else "green"][0]

    #Style.
    plt.style.use('dark_background')
    plt.rc('grid', linestyle="--", color='gray')
    plt.rc('ytick', labelsize=13, color='white')
    plt.rc('xtick', labelsize=13, color = color)
    
    #Line subplots in a figure.
    fig, ax = plt.subplots(figsize = (18, 10))
    #Simulations. 
    simulations.plot(ax = ax, xlabel = xlabel, ylabel = ylabel, title = ("Monte Carlo simulations"), linewidth = 0.15).legend().remove()
    
    #capital_lines, negative line & win/loss for simulations. 
    plt.axhline(y = i_capital, color = "white", linewidth = .8)
    plt.axhline(y = f_capital, color = color, linewidth = .8)
    plt.axhline(y = 0, color = color, linewidth = .4, linestyle = "--")
    plt.axhspan(i_capital, f_capital, facecolor = color, alpha = 0.2)

    #Expected Values.
    E_V.plot(ax = ax, color = color, linewidth = 1)
    #ROI.
    plt.text(0.5, 0.5, "Expected ROI ≈ " + str(ROI), fontsize=13, color=color, transform=ax.transAxes, position = (0.8, 0.65))

    #Style.
    plt.grid(True)
    plt.grid(which='both', color='gray', linestyle='--', alpha = 0.8)
    #x-y ticks.
    ax.xaxis.label.set_size(15), ax.yaxis.label.set_size(15)
    plt.xticks(range(0, len(simulations), 5), [str(i) for i in range(0, len(simulations), 5)])
    plt.yticks(range(0, int(round(simulations.max().max(), 0)), 5), [str(i) for i in range(0, int(round(simulations.max().max(), 0)), 5)])
    
    return plt.show()


def bar_plots(df1, df2, xlabel1, xlabel2, title1, title2):
    """
    Make a bar plot of df.
    """
    #Subplots
    plt.style.use('dark_background')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (20, 8))

    #Bars and background
    df1.plot.bar(ax = ax1, xlabel = xlabel1, ylabel = "density", title = title1).legend().remove()
    df2.plot.bar(ax = ax2, xlabel = xlabel2, ylabel = "density", title = title2).legend().remove()
    #ax1.set_facecolor('xkcd:dark grey'), ax2.set_facecolor('xkcd:dark grey')
    #Set patches for ax1 bars if df1.index is <8 or >8
    [ax1.patches[i].set_facecolor('xkcd:red') if df1.index[i] > 8 else (ax1.patches[i].set_facecolor('xkcd:gray') if df1.index[i] == 8 else ax1.patches[i].set_facecolor('xkcd:green')) for i in range(len(df1.index))]
    [ax2.patches[i].set_facecolor('xkcd:green') if df2.index[i] > 50 else (ax2.patches[i].set_facecolor('xkcd:gray') if df2.index[i] == 50 else ax2.patches[i].set_facecolor('xkcd:red')) for i in range(len(df2.index))]

    #Ticks and real values in bars
    ax1.set_yticklabels(['{:.0f}%'.format(x) for x in ax1.get_yticks()])
    ax2.set_yticklabels(['{:.0f}%'.format(x) for x in ax2.get_yticks()])
    for i in ax1.patches:
        ax1.annotate(str(i.get_height()), (i.get_x(), i.get_height()))
    for i in ax2.patches:
        ax2.annotate(str(i.get_height()), (i.get_x(), i.get_height()))

    ax1.grid(), ax2.grid()
    #Make xlabel and ylabel bigger
    ax1.xaxis.label.set_size(15), ax1.yaxis.label.set_size(15)
    ax2.xaxis.label.set_size(15), ax2.yaxis.label.set_size(15)
    #Make title bigger
    ax1.title.set_size(17), ax2.title.set_size(17)

    plt.show()

