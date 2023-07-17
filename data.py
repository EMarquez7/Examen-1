{""" # -- --------------------------------------------------------------------------------------------------  -- #       
# -- Repository: MonteCarlo-Simulations
# -- Requirements: data.py
# -- Author(s): EstebanMqz
# -- License: CC BY 3.0
# -- Environment: https://github.com/EstebanMqz/MonteCarlo-Simulations/blob/main/data.py
# -- --------------------------------------------------------------------------------------------------  -- #

"""} 
#Dependencies
import glob
import os
# from os import path
import subprocess
import functions as fn 

#Libraries 
import numpy as np
import pandas as pd

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

# -- ----------------------------------------------------------------------------------------------- data ------------------------------------------------------------------------------- -- #

def get_requirements(docstring, ext):
    {"""
    Function to create requirements.txt with required packages & versions to 
    setup a virtual environment for a project's execution.

    Parameters:
    ----------
    + docstring: str
        Docstring of requirements.txt script usually: (repository, requirements, author, license, environment).
    + ext: str
        Extension of the scripts to extract modules used and versions for requirements.txt file creation/update.
    Returns:
    -------
    + requirements.txt: .txt file
        .txt script with modules & versions used in repository to setup or update venv & ensure collaborations.
    """}
 
    subprocess.run(["pipreqs", "--encoding", "utf-8", "./", "--force"])
    
    with open("requirements.txt", "r+") as f:
        old = f.read() 
        f.seek(0) 
        f.write((docstring + old).replace("==", " >= "))
        f.write("jupyter >= 1.0.0 \n")

    with open(glob.glob('*.txt')[0], 'r') as file:
        lines = file.readlines()
        for line in lines:
            if '~' in line:
                lines.remove(line)
            elif 'ipython' in line:
                lines.remove(line)
                lines.append('ipython >= 8.10.0 \n') 

    with open(glob.glob('*.txt')[0], 'w') as file: file.writelines(lines)
    with open(glob.glob('*.txt')[0], 'r') as file: print(file.read())

    script = glob.glob(ext)
    return print("scripts:", script)

def write_docstring(docstring, script):
    {"""
    Inserts introductory docstring in .py scripts for the cwd.

    Parameters:
    ----------
    + docstring: str 
        The docstring to insert.
    + script: str
        The name of the script in cwd.

    Returns:
    -------
    * (docstring: str) + (script: str)
        The docstring inserted in the beginning of the .py script.    
    """}

    cwd = os.getcwd()
    path = os.path.join(cwd, script)

    with open(script, "r+") as f:
        old = f.read()

        if str(docstring) not in old:
            f.seek(0)
            f.write(str('{""" ') + docstring + str('"""} ') + '\r' + old)
        else:
            pass

    return print(str('Succesfully created docstring for: ') + os.path.join('.', script))

def coin_game_sim(i_capital, bet, n_tosses, prize, i_tosses_counter, n_sim):
    {"""Creates a dataframe of n simulations of the coin game for n_tosses.
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
    """}
    
    simulation_arr=[fn.coin_game(i_capital, bet, n_tosses, prize, i_tosses_counter) for i in range(n_sim)]
    
    df = pd.DataFrame([i.iloc[:,0].values for i in simulation_arr])
    df.columns = [str(i) for i in range(1, n_tosses+1)]
    df.index.name = 'Sim'
    df.rename(columns={str(n_tosses): n_tosses}, inplace=True)

    return df

def frequencies(MC):
    {"""
    Calculate the frequencies of simulations of events in a pd.DataFrame.
    
    Parameters
    ----------
    + df : pd.DataFrame
        DataFrame with simulation of events (df.T == df).
    Returns
    -------
    + pd.DataFrame
        DataFrame with the frequencies.
    """}

    N = MC.shape[0] if MC.shape[0] > MC.shape[1] else MC.shape[1]
    if N == MC.shape[0]:
        unique, counts = np.unique(MC.iloc[:, -1], return_counts=True)
    else:
        unique, counts = np.unique(MC.iloc[-1], return_counts=True)

    df_freq = pd.DataFrame({'$x_n$': unique, 'frequency': counts}).set_index('$x_n$').sort_values(by='$x_n$', ascending=True)
    df_freq['$f(x)$'] = df_freq['frequency'] / N
    df_freq['$F(x)$'] = df_freq['frequency'].cumsum() / N
    
    return df_freq

