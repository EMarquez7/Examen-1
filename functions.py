{""" # -- --------------------------------------------------------------------------------------------------  -- #       
# -- Repository: MonteCarlo-Simulations
# -- Requirements: functions.py
# -- Author(s): EstebanMqz
# -- License: CC BY 3.0
# -- Environment: https://github.com/EstebanMqz/MonteCarlo-Simulations/blob/main/functions.py
# -- --------------------------------------------------------------------------------------------------  -- #

"""} 
#Dependencies
from os import path
import glob
import subprocess
import visualizations as vs
import data as dt

#Libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from random import randrange

import IPython.display as d
from tabulate import tabulate

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

# -- ----------------------------------------------------------------------------------------------- functions ------------------------------------------------------------------------------- -- #

def docstring(repository, requirements, author, license, environment):
    {"""
    This function creates a docstring to introduce a script (.py, .txt, .rmd, .m , etc.)

    Parameters:
    ----------
    + repository: str
        Name of the repository.
    + script: str
        Name of the script where the docstring is introduced.
    + author: str
        Contact of the author(s) of the repository.
    + license: str
        License of the repository.
    + environment: str
        Remote of the script.
    Returns:
    -------
    + docstring: str
        Introductory docstring of a script in a repository.
    """}
    return (f"""# -- --------------------------------------------------------------------------------------------------  -- #       
# -- Repository: {repository}
# -- Requirements: {requirements}
# -- Author(s): {author}
# -- License: {license}
# -- Environment: {environment}
# -- --------------------------------------------------------------------------------------------------  -- #
\n""")


def coin_game(initial_cap, bet, n_tosses, prize, start):
    {"""
    Simulates a coin game where the player tries to win by tossing coins.
    The player wins if the difference between the number of heads and tails is 3,
    and loses if the difference while it is lower, counters are reset after each win.

    Parameters:
    ----------
    + initial_cap: int
        The initial capital of the player.
    + bet: int
        The amount of money that the player bets on each coin toss.
    + n_tosses: int
        The number of coin tosses.
    + prize: int
        The amount of money that the player wins if the coin toss is heads.
    + start: int
        The starting value of the variables.
    Returns:
    -------
    + capital: numpy.ndarray
        The capital of the player at each coin toss.
    """}

    capital = np.zeros(n_tosses) 
    heads = np.zeros(n_tosses) 
    tails = np.zeros(n_tosses)
    diff = np.zeros(n_tosses) 
    tosses = np.zeros(n_tosses)

    capital[0] = initial_cap 
    heads[0] = start
    tails[0] = start 
    diff[0] = start 
    tosses[0] = start

    def fill_vector(i):
        nonlocal capital 
        nonlocal heads
        nonlocal tails
        nonlocal diff
        nonlocal tosses

        if randrange(2) == 0: 
            heads[i+1] = heads[i] + 1 
            tails[i+1] = tails[i]     
            diff[i+1] = abs(tails [i+1] - heads [i+1] ) 
            tosses[i+1] = tosses[i] + 1 	
        else:
            tails[i+1] = tails[i] + 1 
            heads[i+1] = heads[i] 
            diff[i+1] = abs(tails [i+1] - heads [i+1] ) 
            tosses[i+1] = tosses[i] + 1
 
        if diff[i] < 3: 
                capital[i + 1] = capital[i] - bet
               
        if diff[i] == 3: 
                capital[i + 1] = capital[i] + prize
                heads[i+1] = start
                tails[i+1] = start
                diff[i+1] = start
             
    [fill_vector(i) for i in range(n_tosses - 1)]

    capital = pd.DataFrame(capital)
    capital.columns = ['Capital']
    capital.index.name = 'Tosses'
    capital.index = capital.index + 1

    return capital
