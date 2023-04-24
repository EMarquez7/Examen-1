"""
# -- ------------------------------------------------------------------------------------------------------------------------ -- #   
# -- project: MonteCarlo-Simulations                                                                                            -- #           
# -- script: data.py : Python script with data functionality for the project                                                  -- #                 
# -- author: EstebanMqz                                                                                                       -- #  
# -- license: CC BY 3.0                                                                                                       -- #
# -- repository: https://github.com/EstebanMqz/MonteCarlo-Simulations/blob/main/data.py                                          -- #           
# -- ------------------------------------------------------------------------------------------------------------------------ -- #  
"""

from os import path
#Dependencies
import functions as fn
import visualizations as vs
import main 
#Libraries in dt
import pandas as pd


def library_install(requirements_txt):
    """Install requirements.txt file."""
    import os
    import warnings
    warnings.filterwarnings("ignore")
    os.system(f"pip install -r {requirements_txt}")
    print("Requirements installed.")
    with open("requirements.txt", "r") as f:
        print(f.read())


def coin_game_sim(i_capital, bet, n_tosses, prize, i_tosses_counter, n_sim):
    """Creates a dataframe of n simulations of the coin game for n_tosses.
    Parameters
    ----------
    i_capital : int
        The initial capital of the player.
    bet : int
        The amount of money that the player bets per coin toss.
    n_tosses : int
        The number of coin tosses in each simulation.
    prize : int
        The amount of money that the player wins if the coin toss is heads.
    i_tosses_counter : int
        The number of tosses.
    n : int
        The number of simulations.
    Returns
    -------
    df : pandas.DataFrame
        A dataframe of n simulations for coin games played.
    """
    
    #Create an array of n simulations of the coin game for n_tosses.
    simulation_arr=[fn.coin_game(i_capital, bet, n_tosses, prize, i_tosses_counter) for i in range(n_sim)]

    #Create dataframe from simulations.
    df = pd.DataFrame([i.iloc[:,0].values for i in simulation_arr])
    #Rename columns and index.
    df.columns = [str(i) for i in range(1, n_tosses+1)]
    #Index and last column name
    df.index.name = 'Sim'
    df.rename(columns={str(n_tosses): n_tosses}, inplace=True)

    return df
