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
#pd options
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_rep', True)
pd.set_option('display.width', None)

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
    }

    with open("requirements.txt", "w") as f:
        f.write(docstring)
        for key, value in requirements.items():
            f.write(f"{key} {value} \n")
        #MODIFY THIS IF YOU IMPORT OTHER LIBRARIES
        f.write("jupyter >= 1.0.0")
        
    #Link to requirements.txt
    print("requirements.txt file is created, it's in user's local path:", path.abspath("requirements.txt"))
    

