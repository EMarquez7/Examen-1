"""
# -- ------------------------------------------------------------------------------------------------------------------------ -- #   
# -- project: MonteCarlo-Simulations                                                                                             -- #           
# -- script: functions.py : Python script with general functions.                                                             -- #                 
# -- author: EstebanMqz                                                                                                       -- #  
# -- license: CC BY 3.0                                                                                                       -- #
# -- repository: https://github.com/EstebanMqz/MonteCarlo-Simulations/blob/main/functions.py                                     -- #           
# -- ------------------------------------------------------------------------------------------------------------------------ -- #  
"""

from os import path
#Dependencies
import visualizations as vs
import data as dt
import main 
#Libraries in fn
import pandas as pd
import numpy as np
from random import randrange

#Define empty docstring
docstring = ""

def get_requirements(docstring):
    # @MODIFY here if you import other libraries.
    import numpy as np
    import pandas as pd
    import matplotlib as plt
    from random import randrange

    """
    Get versions of imported libraries and create "requirements.txt" file for a project environment setup.
    Note: Libraries and requirements dictionary must be imported WITHIN the function and modified accordingly (@MODIFY)  

    Parameters
    ----------
    docstring: str
        Docstring of requirements.txt script in a project.
    Returns
    -------
    requirements.txt
        File with libraries and their respective versions for a project environment setup.
    """

    # @MODIFY this dictionary if you import other libraries.
    requirements = {
        "numpy >=": np.__version__,
        "pandas >=": pd.__version__,
        "matplotlib >=": plt.__version__,
        "IPython.display >=": "8.12.0",
    }

    with open("requirements.txt", "w") as f:
        f.write(docstring)
        for key, value in requirements.items():
            f.write(f"{key} {value} \n")
        #MODIFY THIS IF YOU IMPORT OTHER LIBRARIES
        f.write("jupyter >= 1.0.0 \n")
        f.write("IPython >=" "8.12.0 \n")
        f.write("tabulate >= 0.9.0 \n")

    print("requirements.txt file created in local path:", path.abspath("requirements.txt"))
    

def coin_game(initial_cap, bet, n_tosses, prize, start):
    """
    Simulates a coin game where the player tries to win by tossing coins.
    The player wins if the difference between the number of heads and tails is 3,
    and loses if the difference while it is lower, counters are reset after each win.

    Parameters
    ----------
    initial_cap : int
        The initial capital of the player.
    bet : int
        The amount of money that the player bets on each coin toss.
    n_tosses : int
        The number of coin tosses.
    prize : int
        The amount of money that the player wins if the coin toss is heads.
    start : int
        The starting value of the variables.
    Returns
    -------
    capital : numpy.ndarray
        The capital of the player at each coin toss.
    """

    #Vectors of zeros for filling.
    capital = np.zeros(n_tosses) 
    heads = np.zeros(n_tosses) 
    tails = np.zeros(n_tosses)
    diff = np.zeros(n_tosses) 
    tosses = np.zeros(n_tosses)

    #Variables at game start.
    capital[0] = initial_cap 
    heads[0] = start
    tails[0] = start 
    diff[0] = start 
    tosses[0] = start

    #Working with arrays outside function: nonlocal variables.
    def fill_vector(i):
        nonlocal capital 
        nonlocal heads
        nonlocal tails
        nonlocal diff
        nonlocal tosses

        #Coin toss = Heads.
        if randrange(2) == 0: 
            heads[i+1] = heads[i] + 1 
            tails[i+1] = tails[i]     
            diff[i+1] = abs(tails [i+1] - heads [i+1] ) 
            tosses[i+1] = tosses[i] + 1 	
        else:
            #Coin toss = Tails.
            tails[i+1] = tails[i] + 1 
            heads[i+1] = heads[i] 
            diff[i+1] = abs(tails [i+1] - heads [i+1] ) 
            tosses[i+1] = tosses[i] + 1

        #Lose bet ($1): Difference in tossed coins (H & T) < 3.         
        if diff[i] < 3: 
                capital[i + 1] = capital[i] - bet

        #Win bet ($8): Difference in tossed coins (H & T) = 3.                  
        if diff[i] == 3: 
                capital[i + 1] = capital[i] + prize
                #Reset (H & T). 
                heads[i+1] = start
                tails[i+1] = start
                diff[i+1] = start
        
    #Fill variables with values.           
    [fill_vector(i) for i in range(n_tosses - 1)]

    #Make a Dataframe of resulting capital per toss. 
    capital = pd.DataFrame(capital)
    capital.columns = ['Capital']
    capital.index.name = 'Tosses'
    capital.index = capital.index + 1

    return capital
