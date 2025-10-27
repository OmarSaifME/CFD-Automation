# CFD-Automation
A Journal Script for Automated Simulation and Post-Processing for 2D Airfoil Study in ANSYS Fluent

**Overview**

This repository hosts automated scripts for simulation and post-processing of a single run (specific AoA) CFD study for a 2D airfoil (or any other 2D object). The script carefully excludes the step to select the governing equation, but future updates might add these steps if necessary. Additionally, you can find technical documentation and supplementary Python scripts (more about it on the pdf file) for your own study. Additional files will be added in the future (with validated datasets), as the entire workflow is going through multiple testing and iteration at the time of this commit. 

**Features**
- **Multiple Journal File**: There are a couple of .jou file. One for first run, the other for subsequent runs for a single project. More about it can be found on the pdf file.
- **Supplimentary Python Script**: In order to manipulate AoA between runs, a supplementary Python script has also been added, where the user can extract key values and plug them into the journal (details can be found on the pdf file) for multiple simulation runs, each mimicking different *Angle of Attack* for the study.
- **Python Script for Re Conversion**: Developed for a different project, this Python script can take input of critical variables and convert Re numbers to fluid velocity, and vice versa. A simple calculator script that the user could find useful. 
- **Portable Document Format File**: A pdf file has also been added as a *tutorial* for first time users. However, readers are expected to possess prior working knowledge of ANSYS Fluent, as this documentation assumes familiarity with essential computational fluid dynamics concepts and does not address foundational simulation techniques.

**Thank You** for stopping by. I hope this repository helps you in your CFD study. 
