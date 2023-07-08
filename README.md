### **MonteCarlo Simulation** <br><br>

<Details>
<Summary> <i>Tools:</i> </Summary>
  
##### Actions:  [![Repo-Visualization-Badge](https://img.shields.io/badge/Action-Visualization-020521?style=square&logo=github&logoColor=white)](https://githubnext.com/projects/repo-visualization)
##### Main Text-Editor:  [![VSCode-Badge](https://img.shields.io/badge/VSCode-007ACC?style=square&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)  [![Jupyter-Badge](https://img.shields.io/badge/Jupyter-F37626?style=square&logo=Jupyter&logoColor=white)](https://jupyter.org/try)
##### Language:  [![Python-Badge](https://img.shields.io/badge/Python-2b6dd6.svg?style=square&logo=Python&logoColor=green)](https://www.python.org)[![Markdown-Badge](https://img.shields.io/badge/Markdown-000000.svg?style=square&logo=Markdown&logoColor=white)](https://www.markdownguide.org)[![yaml-Badge](https://img.shields.io/badge/YAML-000000?style=square&logo=yaml&logoColor=red)](https://yaml.org)
##### Libraries:  [![Numpy-Badge](https://img.shields.io/badge/Numpy-013243?style=square&logo=numpy&logoColor=white)](https://numpy.org)  [![Pandas-Badge](https://img.shields.io/badge/Pandas-150458?style=square&logo=pandas&logoColor=white)](https://pandas.pydata.org)  [![Random-Badge](https://img.shields.io/badge/Random-000000?style=square&logo=python&logoColor=white)](https://docs.python.org/3/library/random.html)  [![Matplotlib-Badge](https://img.shields.io/badge/Matplotlib-40403f?style=square&logo=python&logoColor=blue)](https://matplotlib.org)
##### Venv: [![Gists](https://img.shields.io/badge/Gists-Environment-010b38?style=square&logo=github&logoColor=black)](https://gist.github.com/EstebanMqz/f30253a8bf8cb50b4510aa8bda10bf7c) [![Gists](https://img.shields.io/badge/Gists-Docstrings-010b38?style=square&logo=github&logoColor=black)](https://gist.github.com/EstebanMqz/6dd3ae6038e5aeec223e80d9b5db3977)
##### Interface:  [![React-Badge](https://img.shields.io/badge/React-61DAFB?style=square&logo=react&logoColor=black)](https://create-react-app.dev)
##### Version Control:  [![GitHub-Badge](https://img.shields.io/badge/GitHub-100000?style=square&logo=github&logoColor=white)](https://github.com)  [![Git-Badge](https://img.shields.io/badge/Git-F05032.svg?style=square&logo=Git&logoColor=white)](https://git-scm.com)
[![Git-Commands](https://img.shields.io/badge/Git%20Commands-gray?style=square&logo=git&logoColor=white)](https://github.com/EstebanMqz/Git-Commands)
##### License: [![Creative Commons BY 3.0](https://img.shields.io/badge/License-CC%20BY%203.0-yellow.svg?style=square&logo=creative-commons&logoColor=white)](https://creativecommons.org/licenses/by/3.0/)
</Details>

<Details>
<Summary> <i>Contact:</i> </Summary>
  
[![Website](https://img.shields.io/badge/Website-ffffff?style=square&logo=opera&logoColor=red)](https://estebanmqz.com) [![LinkedIn](https://img.shields.io/badge/LinkedIn-041a80?style=square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/esteban-m65381722210212839/) [![Portfolio](https://img.shields.io/badge/Github-Portfolio-010b38?style=square&logo=github&logoColor=black)](https://estebanmqz.github.io/Portfolio/) [![E-mail](https://img.shields.io/badge/Business-Mail-052ce6?style=square&logo=mail&logoColor=white)](mailto:esteban@esteban.com)

![GitHub Logo](https://github.com/EstebanMqz.png?size=50) [![Github](https://img.shields.io/badge/Github-000000?style=square&logo=github&logoColor=white)](https://github.com/EstebanMqz)
</Details>

<Details> <Summary> <i> Repo Visualization: </i> </Summary>

<a name = "Repo-Visualization"></a>

[![Repository](https://img.shields.io/badge/Repository-0089D6?style=square&logo=microsoft-azure&logoColor=white)](https://mango-dune-07a8b7110.1.azurestaticapps.net/?repo=EstebanMqz%2FMonteCarlo-Simulation) [![Jupyter](https://img.shields.io/badge/Render-nbviewer-000000?style=square&logo=jupyter&logoColor=orange)](https://nbviewer.org/github/EstebanMqz/MonteCarlo-Simulation/blob/main/MC-Simulation.ipynb)
  
<img src="diagram.svg" width="280" height="280">
</Details> 
<br>

<b>Description:</b><br>
[Github-app parse](https://github.com/EstebanMqz/MonteCarlo-Simulation/blob/main/images/Description.jpg)

This repository illustrates how MonteCarlo calculates crucial decision-making tools from simulations $X \sim f(X)$ like [$E[X]$](README.md#references):

$$E[X] \approx \frac{1}{N} \sum_{i=1}^{N} x_i = \mu_{M.C}$$

<b>$X$</b> = <i>Random Variable from simulations.</i> <br>
<b>$\mu_{M.C}$</b> = <i>Mean of the MonteCarlo Simulations.</i><br>
<b>$N$</b> = <i>No° of Simulations.</i>

$\&$ [$E[RoI]$](README.md#references) and probabilities with their density function [$f_X(x)$](README.md#references) $\&$ <i>cumulative distribution</i> [$F_X(x)$](README.md#references):

In this case, with an expected Capital per game in a set of games $(n=100)$ planned to be played in a <i>Casi-no</i>:

$$E[X_1]+ E[X_2] + ... +E[X_n] = \mu_{M.C{_1}} + \mu_{M.C{_2}} + ... + \mu_{M.C_n}$$

<b>$X$</b> = <i>Random Variable from simulations.</i> <br>
<b>$\mu_{M.C}$</b> = <i>Mean of the MonteCarlo Simulations.</i><br>
<b>$N$</b> = <i>No° of Simulations.</i>

*(See [Repo Visualization](#Repo-Visualization) → render)* for more details.

<Details> <Summary> <b>  Results: </b> </Summary>
  
The Expectancy of the Capital could have the following outcomes used for $E[X]$ $\&$ $E[RoI]$:<br>
<img src="/images/MC_Sim.jpg" width="800" height="463"><br>

At the $100_{th}$ the Win chances are:

<img src="/images/W-L.jpg" width="197" height="87"><br>

Probabilities are illustrated with their frequencies:

<img src="/images/fx.jpg" width="260" height="491"><br>

Resulting prob. density functions $f(X)$ on Wins & $E[X]$ should be the same as $X$ is discrete:
<img src="/images/histogram.jpg" width="896" height="402">
</Details> 

###### References:<br>

+ [Monte Carlo Estimator](http://www.mit.edu/~kircher/sim.pdf)<br>
+ [$E[X]$](https://en.wikipedia.org/wiki/Expected_value) ,&nbsp; [$RoI$](https://en.wikipedia.org/wiki/Rate_of_return)<br>
+ [$f_X(x)$](https://en.wikipedia.org/wiki/Probability_density_function)<br>
+ [$F_X(x)$](https://en.wikipedia.org/wiki/Cumulative_distribution_function)<br>
+ [`random.randrange`](https://docs.python.org/3/library/random.html#random.randrange)<br>
+ [LaTeX](https://en.wikipedia.org/wiki/List_of_mathematical_symbols_by_subject)<br>
