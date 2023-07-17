{""" # -- --------------------------------------------------------------------------------------------------  -- #       
# -- Repository: MonteCarlo-Simulations
# -- Requirements: visualizations.py
# -- Author(s): EstebanMqz
# -- License: CC BY 3.0
# -- Environment: https://github.com/EstebanMqz/MonteCarlo-Simulations/blob/main/visualizations.py
# -- --------------------------------------------------------------------------------------------------  -- #

"""}
#Dependencies
import os

#Libraries 
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

# -- ----------------------------------------------------------------------------------------------- visualizations ------------------------------------------------------------------------------- -- #

def MC_plot(MC, EX, xlabel , ylabel, img_name, ext):
    {"""Plots line plots of Events for all N Monte Carlo simulations, retrieves Expetancy of random variables X & Rate of Return.
     
    Parameters
    ----------
    MC : pd.DataFrame
        Dataframe of MonteCarlo Simulations (cols.) from a set of events (rows).
    EX : pandas.DataFrame
        Dataframe of E[X] & E[RoI] on cols. 1,2: EX['$E[X]$'], EX['$E[RoI]$'].
        Note: EX display is on markdown.
    xlabel, ylabel : str
        Labels of the x-axis, y-axis.
    img_name : str
        Name of the image file to be saved.
    ext : str
        Extension of the figure  Use 'jpg', 'png', 'jpeg' or 'svg' as as extension for the figure to save in images.
        Returns
    -------
    line_plot : matplotlib.pyplot
        Plot of N simulations with X, E[X] & RoI.
    """}

    RoI = EX['$E[RoI]$'].iloc[-1].round(6)
    N = MC.shape[0] if MC.shape[0] > MC.shape[1] else MC.shape[1]
    color = ["red" if RoI < 0 else "green"][0]

    plt.style.use('dark_background')
    plt.rc('grid', linestyle="--", color='gray')
    plt.rc('ytick', labelsize=13, color=color), plt.rc('xtick', labelsize=13, color = 'white')
   
    fig, ax = plt.subplots(figsize = (18, 10))
    ax.set_facecolor('black')

    MC.plot(ax = ax, title = (str(N) + " Simulation(s)"), linewidth = 0.15).legend().remove()
   
    plt.axhline(y = EX['$E[X]$'].iloc[0], color = "white", linewidth = .8)
    plt.axhline(y = EX['$E[X]$'].iloc[-1], color = color, linewidth = .8)
    plt.axhline(y = 0, color = color, linewidth = .5)
    plt.axhspan(EX['$E[X]$'].iloc[0], EX['$E[X]$'].iloc[-1], facecolor = color, alpha = 0.2)
    EX['$E[X]$'].plot(ax = ax, color = color, linewidth = 1)
    plt.text(0.5, 0.5, "$E[RoI]$ ≈ " + str(RoI), fontsize=13, color=color, transform=ax.transAxes, position = (0.8, 0.65))

    plt.grid(True), plt.grid(which='both', color='gray', linestyle='--', alpha = 0.8)
    
    ax.set_xlabel(xlabel), ax.set_ylabel(ylabel), ax.xaxis.label.set_color('teal'), ax.yaxis.label.set_color('teal')
    ax.xaxis.label.set_size(15), ax.yaxis.label.set_size(15), ax.title.set_size(20), ax.title.set_color('teal')
    
    try:
        os.mkdir('images')
    except FileExistsError:
        pass
    if ext == 'jpg' or ext == 'png' or ext == 'jpeg' or ext == 'svg':
        plt.savefig(f"images/{img_name}.{ext}", dpi = 300, bbox_inches='tight')
        print(f"Figure successfully created / overwritten in ./images/{img_name}.{ext}")
    else:
        print("Img format not supported. Use 'jpg', 'png', 'jpeg' or 'svg' as extension for the figure to be saved.")

    return plt.show()

def bar_plots(df1, df2, xlabel1, xlabel2, title1, title2, img_name, ext):

    {"""
    Make a bar plot of dataframes frequencies with Red-Gray-Green colors for resulting E[X].

    Parameters
    ----------
    df1 : pandas.DataFrame
        First dataframe to be plotted.
    df2 : pandas.DataFrame
        Second dataframe to be plotted.
    xlabel1 : str
        Label for the x-axis of the first plot.
    xlabel2 : str
        Label for the x-axis of the second plot.
    title1 : str
        Title for the first plot.
    title2 : str
        Title for the second plot.
    img_name : str
        Name of the image file to be saved.
    ext : str
        File extension for the image file to be saved. Must be one of 'jpg', 'png', 'jpeg', or 'svg'.

    Returns
    -------
    None
        Displays the plot and saves it to a file in the 'images' directory.
    """}
    plt.style.use('dark_background')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (20, 8))

    df1.plot.bar(ax = ax1, xlabel = xlabel1, ylabel = "density", title = title1).legend().remove()
    df2.plot.bar(ax = ax2, xlabel = xlabel2, ylabel = "density", title = title2).legend().remove()

    [ax1.patches[i].set_facecolor('xkcd:red') if df1.index[i] <= 10 else (ax1.patches[i].set_facecolor('xkcd:gray') if df1.index[i] == 11 else ax1.patches[i].set_facecolor('xkcd:green')) for i in range(len(df1.index))]
    [ax2.patches[i].set_facecolor('xkcd:green') if df2.index[i] > 50 else (ax2.patches[i].set_facecolor('xkcd:gray') if df2.index[i] == 50 else ax2.patches[i].set_facecolor('xkcd:red')) for i in range(len(df2.index))]

    ax1.set_yticklabels(['{:.1f}%'.format(x/100) for x in ax1.get_yticks()])
    ax2.set_yticklabels(['{:.1f}%'.format(x/100) for x in ax2.get_yticks()])
    for i in ax1.patches:
        ax1.annotate(str(i.get_height()), (i.get_x(), i.get_height()))
    for i in ax2.patches:
        ax2.annotate(str(i.get_height()), (i.get_x(), i.get_height()))

    ax1.grid(), ax2.grid()
    ax1.xaxis.label.set_size(15), ax1.yaxis.label.set_size(15)
    ax2.xaxis.label.set_size(15), ax2.yaxis.label.set_size(15)
    ax1.title.set_size(17), ax2.title.set_size(17)
    
    if ext == 'jpg' or ext == 'png' or ext == 'jpeg' or ext == 'svg':
        plt.savefig(f"images/{img_name}.{ext}", dpi = 300, bbox_inches='tight')
        print(f"Figure successfully created / overwritten in ./images/{img_name}.{ext}")
    else:
        print("Img format not supported. Use 'jpg', 'png', 'jpeg' or 'svg' as extension for the figure to be saved.")

    return plt.show()



