# You've arrived at week 0's assignment!


The assignment this week consists of getting python installed on your local computer (should that be available to you), reading, and completing a Jupyter Notebook by responding to several prompts.

For the installation of python, we will use the free python module/package manager "[Anaconda](https://www.anaconda.com/products/individual)."  You will install either the full Anaconda platform (recommended if you have room on your computer), or the smaller "[Miniconda](https://docs.conda.io/en/latest/miniconda.html#)." Then you will set up what is known as an "environment" to keep the modules necessary for spatial data analysis accessible.

## Here's some more detail on setting up and installing python:
1. _Download and install the [Anaconda individual edition](https://docs.anaconda.com/anaconda/install/)_ or [Miniconda](https://docs.conda.io/en/latest/miniconda.html#latest-miniconda-installer-links)<br/>
    - For more on choosing between these installation packages, see [this link](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html#anaconda-or-miniconda).
    - Anaconda/conda both installs python and creates a system by which you can expand python's functionality through "packages" or "modules." You can [learn more about managing and installing packages here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html#).<br/>
    - If you're given the option, you'll likely want a 64 bit version (as compared to a 32 bit version). If given the option, use python 3, not python 2. python 2 is obsolete. Tim doesn't have any experience with PyCharm, and so hasn't chosen to install it himself.<br/>
    - **Before you proceed,** review the [Getting Started with Conda website](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html).<br/>
  
  
2. _Set up your conda environments_<br/>
    - Scientific computing with python is done using "packages" or "modules."  Some combinations of modules might be incompatible.  Anaconda helps maintain mutually consistent modules, but environments take this a step further.  By creating separate "environments," you create different virtual _workshops_ or _sandboxes_ in which all the tools are designed to work well together, and not conflict.<br/>
    - Download the file GISenv21b.yml to your computer.  This file specifies what modules will be installed in this environment.
    - Set up the GISenv21b environment.  In the directory to which you've downloaded `GISenv21b`, type `conda env create -f GISenv21b.yml`.  Be patient.  There are a lot of components for this environment and it can take 45 minutes for the environment to be "solved," which means that compatible versions of all the modules have been identified.  Once the environment is set up, you will have access to a suite of python modules useful for working with spatial data, but _only when the environment is active (see below)._
    - Some of the other environments that the UI Glacier Dynamics Lab (and Tim personally) uses for his projects are hosted on github [here](https://github.com/tbartholomaus/conda_envs).<br/>
    - You can also [learn more about conda environments below](https://github.com/tbartholomaus/uiglaciology/blob/master/content/3-code.md#environments-internally-consistent-sets-of-python-modules).<br/>


3. _Start coding_<br/>
    - Activate your newly created conda environment: `conda activate GISenv21b`
    - Now you're ready to start coding in python!  
    - Open either Jupyter Lab to start an interface for coding pythong. 


## Reading Assignment
### 1. A Whirlwind Tour of Python (~2-4 hours)
* Work your way through Jake VanderPlas’ excellent “Whirlwind Tour of Python”: https://jakevdp.github.io/WhirlwindTourOfPython/. To do so, first download the notebooks from github.
    * Go to https://github.com/jakevdp/WhirlwindTourOfPython and click on the green "Code" button
    * Download the zip file somewhere within your directory for this class and unzip it.
* Work through the notebooks, taking some time to experiment along the way (don’t just shift-Enter without reading text or absorbing concepts)
    * Can skip sections on Python installation and conda - we’ve taken care of this with the class Jupyterhub setup, and we will revisit conda later in the quarter
    * Note that we are exclusively using Python3 in this class (but good to know about potential issues with Python2 compatibility)
    * If you’re short on time (or feeling overwhelmed), you can skip sections 09 (Errors and Exceptions), 12 (Generators and Generator Expressions) and 14 (Strings and Regular Expressions)
      * Note: chapter numbers in the book vs. the interactive notebooks are slightly different
* Note that you can also view rendered versions of the notebooks on the original github page, but please take advantage of the interactive notebooks - try changing some things and rerunning


### Optional
If this is too basic (or you’re curious), try one or more of the following:
* Learn new iPython/Jupyter keystrokes and magic functions
* Read the official Python documentation: https://docs.python.org/3/index.html. 
* Review documentation and source code for the Python standard library:
    * This is the definition of pure Python, and a great reference of how to write clean, efficient, well-documented Python code.
    * https://docs.python.org/3/library/
    * https://github.com/python/cpython/tree/master/Lib 
    * For example, when you `import os`, here's what you're running: https://github.com/python/cpython/blob/master/Lib/os.py
* Review the Python style guide: https://www.python.org/dev/peps/pep-0008/

## Coding Assignment
This coding assignment is at https://github.com/tbartholomaus/GIS_programming_F21/blob/main/weeks/wk0_getting_started/assignment/Assignment0.ipynb. Please work through this notebook and complete the few cells which require your responses.
