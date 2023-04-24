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


def line_plot(simulations, E_V1, xlabel , ylabel, i_capital, f_capital, sim):
    """Plots a line plot of the data over time in n Monte Carlo simulations.
    Parameters
    ----------
    simulation : pandas.DataFrame
        The result of the Monte Carlo simulation.
    xlabel : str
        The label of the x-axis.
    ylabel : str
        The label of the y-axis.
    sim : int
        The number of simulations to make.
    i_capital : int
        The initial value of the variable to be simulated.
    f_capital : int
        The final value of the variable simulated.
    Returns
    -------
    line_plot : matplotlib.pyplot
        A line plot of simulations time series. 
    """

    #If ROI is negative make the color red, otherwise green.
    ROI = round((E_V1.iloc[-1][0] / E_V1.iloc[0][0]) - 1, 4)
    if ROI < 0:
        color = "red"
    else:
        color = "green"
    #Style
    plt.style.use('dark_background')
    plt.rc('grid', linestyle="--", color='gray')
    plt.rc('ytick', labelsize=13, color='lightgreen')
    plt.rc('xtick', labelsize=13, color = color)
    
    #Line subplots in a figure.
    fig, ax = plt.subplots(figsize = (18, 10))
    #Simulations.
    simulations.plot(ax = ax, xlabel = xlabel, ylabel = ylabel, title = ("Expected Value of Capital over time in " + str(sim)
                    + " Monte Carlo simulations went from " + str(i_capital)+ " to: " + str(f_capital)), linewidth = 0.125)
    #Expected Values and ROI.
    E_V1.plot(ax = ax, color = color, linewidth = 1, label = "Expected Value")
    plt.text(0.5, 0.5, "Expected ROI ≈ " + str(ROI), fontsize=15, color=color)

    #Style
    plt.legend().remove()
    plt.grid(True)

    return plt.show(), simulations


def hist_plot(simulation, xlabel , ylabel, n_games, n, i_capital, color):
    """Plots a hist plot of the final capital in Monte Carlo simulations.
    Parameters
    ----------
    coin_simulation : pandas.DataFrame
        The capital of the player at each coin toss.
    xlabel : str
        The label of the x-axis.
    ylabel : str
        The label of the y-axis.
    n_games : int
        The number of games played.
    n : int
        The number of simulations of n games planned to play.
    i_capital : int
        The initial capital of the player.
    f_capital : int
        The final capital of the player.
    Returns
    -------
    line_plot : matplotlib.pyplot
        The line plot of the capital over time in n Monte Carlo simulations.
    """

    plt.title("Final capital after planned " + str(n_games) + " games with starting capital of " + str(i_capital)
          + " calculated with " + str(n) + " planned played games simulations (Monte Carlo")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    #Hist plot
    plt.hist(simulation, bins = 20, color = color, width = 5, edgecolor='black', density=True)[2]
    plt.gcf().set_size_inches(12, 8)

    return plt.show()
