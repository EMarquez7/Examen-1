### **MonteCarlo Simulation** <br><br>

<Details> <Summary> <i> <font color= 'orange'> Files Visualization: </font> </i> </Summary>

[![Repository](https://img.shields.io/badge/Repository-0089D6?style=square&logo=microsoft-azure&logoColor=white)](https://mango-dune-07a8b7110.1.azurestaticapps.net/?repo=EstebanMqz%2FMonteCarlo-Simulation) [![Jupyter](https://img.shields.io/badge/Render-nbviewer-000000?style=square&logo=jupyter&logoColor=orange)](https://nbviewer.org/github/EstebanMqz/MonteCarlo-Simulation/blob/main/MC-Simulation.ipynb)

<img src="diagram.svg" width="280" height="280">
</Details> 

#### **Repository Tools:**
<font>
<Details>
<Summary> <b>Click to expand</b> </Summary>

##### Actions:  [![Repo-Visualization-Badge](https://img.shields.io/badge/Action-Visualization-020521?style=square&logo=github&logoColor=white)](https://githubnext.com/projects/repo-visualization)
##### Main Text-Editor:  [![VSCode-Badge](https://img.shields.io/badge/VSCode-007ACC?style=square&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)  [![Jupyter-Badge](https://img.shields.io/badge/Jupyter-F37626?style=square&logo=Jupyter&logoColor=white)](https://jupyter.org/try)
##### Language:  [![Python-Badge](https://img.shields.io/badge/Python-2b6dd6.svg?style=square&logo=Python&logoColor=green)](https://www.python.org)[![Markdown-Badge](https://img.shields.io/badge/Markdown-000000.svg?style=square&logo=Markdown&logoColor=white)](https://www.markdownguide.org)[![yaml-Badge](https://img.shields.io/badge/YAML-000000?style=square&logo=yaml&logoColor=red)](https://yaml.org)
##### Libraries:  [![Numpy-Badge](https://img.shields.io/badge/Numpy-013243?style=square&logo=numpy&logoColor=white)](https://numpy.org)  [![Pandas-Badge](https://img.shields.io/badge/Pandas-150458?style=square&logo=pandas&logoColor=white)](https://pandas.pydata.org)  [![Random-Badge](https://img.shields.io/badge/Random-000000?style=square&logo=python&logoColor=white)](https://docs.python.org/3/library/random.html)  [![Matplotlib-Badge](https://img.shields.io/badge/Matplotlib-40403f?style=square&logo=python&logoColor=blue)](https://matplotlib.org)
##### Interface:  [![React-Badge](https://img.shields.io/badge/React-61DAFB?style=square&logo=react&logoColor=black)](https://create-react-app.dev)
##### Version Control:  [![GitHub-Badge](https://img.shields.io/badge/GitHub-100000?style=square&logo=github&logoColor=white)](https://github.com)  [![Git-Badge](https://img.shields.io/badge/Git-F05032.svg?style=square&logo=Git&logoColor=white)](https://git-scm.com)
[![Git-Commands](https://img.shields.io/badge/Git%20Commands-gray?style=square&logo=git&logoColor=white)](https://github.com/EstebanMqz/Git-Commands)
##### License: [![Creative Commons BY 3.0](https://img.shields.io/badge/License-CC%20BY%203.0-yellow.svg?style=square&logo=creative-commons&logoColor=white)](https://creativecommons.org/licenses/by/3.0/)
</Details>

##### Contact: 
<font>
<Details>
<Summary> <b>Click to expand</b> </Summary>

[![Website](https://img.shields.io/badge/Website-ffffff?style=square&logo=opera&logoColor=red)](https://estebanmqz.com) [![LinkedIn](https://img.shields.io/badge/LinkedIn-041a80?style=square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/esteban-m65381722210212839/) [![Portfolio](https://img.shields.io/badge/Github-Portfolio-010b38?style=square&logo=github&logoColor=black)](https://estebanmqz.github.io/Portfolio/) [![E-mail](https://img.shields.io/badge/Business-Mail-052ce6?style=square&logo=mail&logoColor=white)](mailto:esteban@esteban.com)

![GitHub Logo](https://github.com/EstebanMqz.png?size=50) [![Github](https://img.shields.io/badge/Github-000000?style=square&logo=github&logoColor=white)](https://github.com/EstebanMqz)
</Details>

**Description:**

This repository contains a MonteCarlo simulation in order to obtain Expected Values:<br>
$$E(V) \approx \frac{1}{N_{sim}} \sum_{i=1}^{N_{sim}} V_i=\mu_{M.C}$$
<br>

As well as its $RoI$, Probabilities $P(X)$, from its density function <i>pdf</i> $f(X)$ and cumulative density function $F(X)$.<br>
Fundamental decision making tools made from scripts and snippets.<br>

### **Results:**
Even though ${E(V)}\approx \mu_{M.C}$ in every simulation, there are other values that are possible as well $\forall N_{sim}$ in the Casi-no:<br>
<img src="/images/MC_Sim.jpg" width="800" height="347"><br>

So the Prob. of Win/Lose $\forall N_{sim} = 10000$ are:
<br>

<img src="/images/W-L.jpg" width="197" height="87">

<br>

In this regard, the probability $f(X)$, its cumulative values $F(X)$ and its Expected values $E(V) = \mu_{M.C}$ are:

<img src="/images/fx.jpg" width="260" height="491"> <br>

The histograms for the prob. density function $f(X)$ on the $Win_{Events}$ and $FV$ are illustrated:
<img src="/images/histogram.jph" width="896" height="493">
