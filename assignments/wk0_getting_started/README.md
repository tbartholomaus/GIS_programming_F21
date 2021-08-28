# You've arrived at week 0's first assignment!


This page contains helpful tips for working with software, especially the python programming language.

A table of contents for this page includes:
+ [Python](https://tbartholomaus.github.io/uiglaciology/3-code#python)
  + [How to get started on your personal computer with python, Anaconda, and environments](https://tbartholomaus.github.io/uiglaciology/3-code#how-to-get-started-on-your-personal-computer-with-python-anaconda-and-environments)
  + [Environments: internally consistent sets of python modules](https://tbartholomaus.github.io/uiglaciology/3-code#environments-internally-consistent-sets-of-python-modules)
  + [Preferred python interface](https://tbartholomaus.github.io/uiglaciology/3-code#preferred-python-interface)
  + [Keeping a script running overnight (or other long periods)](https://tbartholomaus.github.io/uiglaciology/3-code#keeping-a-script-running-overnight-or-other-long-periods)
  + [Helpful native Python functions](https://tbartholomaus.github.io/uiglaciology/3-code#helpful-native-python-functions)
+ [Geographic information systems (GIS)](https://tbartholomaus.github.io/uiglaciology/3-code#geographic-information-systems-gis)

# Python
<br/>

## How to get started on your personal computer with python, Anaconda, and environments
Here are four steps you can follow to start working with python:
1. _Download and install the [Anaconda individual edition](https://docs.anaconda.com/anaconda/install/)_<br/>
    - Anaconda/conda both installs python and creates a system by which you can expand python's functionality through "packages" or "modules." You can [learn more about managing and installing packages here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html#).<br/>
    - If you're given the option, you'll likely want a 64 bit version (as compared to a 32 bit version). If given the option, use python 3, not python 2. python 2 is obsolete. Tim doesn't have any experience with PyCharm, and so hasn't chosen to install it himself.<br/>
    - **Before you proceed,** review the [Getting Started with Conda website](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html).<br/>
  

2. _Set up your conda environments_<br/>
    - This step is technically optional, but recommended before you dive into new projects.  It is necessary if you plan to work with Jupyter Lab.<br/>
    - Scientific computing with python is done using "packages" or "modules."  Some combinations of modules might be incompatible.  Anaconda helps maintain mutually consistent modules, but environments take this a step further.  By creating separate "environments," you create different virtual _workshops_ or _sandboxes_ in which all the tools are designed to work well together, and not conflict.<br/>
    - Some of the environments that the UI Glacier Dynamics Lab (and Tim personally) uses for his projects are hosted on github [here](https://github.com/tbartholomaus/conda_envs).<br/>
    - You can also [learn more about conda environments below](https://github.com/tbartholomaus/uiglaciology/blob/master/content/3-code.md#environments-internally-consistent-sets-of-python-modules).<br/>

3. _Start coding_<br/>
    - Open either Spyder or Jupyter Lab to start an interface for coding pythong. [More on these two options below](https://github.com/tbartholomaus/uiglaciology/blob/master/content/3-code.md#preferred-python-interface). If you're just getting started, Tim recommends Jupyter Lab.<br/>

4. _Learning python_<br/>
    - If you're new to programming and want to get started learning the python that's necessary for foundational work in the geosciences, Tim recommends starting with the course [Geo-Python](https://geo-python.github.io) from the University of Helsinki.  The syllabus is excellent, there are videos with instructions, clear text descriptions, and exercises to practice what you're learning. The [Earth Analytics Bootcamp course](https://www.earthdatascience.org/courses/earth-analytics-bootcamp/) from the CU Boulder Earth Lab also is excellent and has an associated online textbook for the course.<br/>
    - Tim has also had students successfully teach themselves python through various online education platforms such as EdX, Coursera, Udemy, and Educative.  Two courses that especially look good, and are targeted towards scientists (as compared to web developers) are [here at Educative](https://www.educative.io/courses/python-for-scientists-and-engineers) and [here at Udemy](https://www.udemy.com/course/python-for-data-science-and-machine-learning-bootcamp).  These courses don't tend to be free (like Geo-Python and Earth Analytics Bootcamp above), but the structure and assignments might work well for some learners. The [python website](https://wiki.python.org/moin/BeginnersGuide) also provides useful tutorials that are helpful for beginners. <br/>
    - Tim's favorite go-to reference manual, with exhaustive examples and suggestions for coding if you're not sure where to start are the [SciPy lectures](https://scipy-lectures.org/). This manual provides a consistent primer for what's involved in python's core functionality and the modules you'll need to do science, but is more like reading a textbook than taking a classs.  You can use the website itself or download the entire lecture set as a 600+ page PDF and scroll through it (Tim's preferred method).  To get going, read and work through Chap 1 ("Python scientific computing ecosystem"), Chap 2 ("The Python language" sections "First Steps," "Basic types," and "Control Flow"), and then all of Chap 4 ("NumPy") and Chap 5 ("Matplotlib"). Don't just skim these sections, but actually have Jupyter Lab or Spyder open and execute the code, experimenting along the way.<br/>
    - Once you are past the basics, googling for answers is essential.  Stack Overflow and Stackexchange are invaluable tools for professional, beginner, and enthusiastic programmers. Both are question and answer platforms used across the programming community to solve coding problems collaboratively.	 They will frequently come up in Google searches.<br/>
    - For learning more advanced topics, such as solving PDEs and matrices, symbolic computing, etc., Tim has had a great experience with the book [Numerical Python by Robert Johansson](https://www.apress.com/us/book/9781484242452).<br/>


## Environments: internally consistent sets of python modules
If you want to use python on kennicott, after you log in, type `conda activate` followed by the name of the environment you'd like to work in.  You might want to append this to the end of your `~/.bashrc` or `~/.bashprofile` file, which is a text file that runs automatically every time you log into kennicott. Different sets of packages for different purposes are organized into specific "environments," which are kept internally consistent.  You can identify the available environments by typing `conda env list`.  In fall 2020, there are four main environments that are available to all users on kennicott: base20 (fundamental, basic scientific computing packages), seisenv20 (for the purpose of working with obspy and seismic data), spatialenv20 (for the purpose of working with spatial data, like shapefiles, geotiffs, and other rasters), and imgenv20 (for image processing with opencv, PIL, etc.).  Each of these environments is maintained [on github as well, here,](https://github.com/tbartholomaus/conda_envs) so you can suggest changes, or download them yourself to have consistent environments on personal and work computers. You can change to one of these environments by typing `conda activate myenv`, in which case you replace `myenv` with the name of the environment you want to use. If there are python modules you'd like to use that don't fall in one of these categories, you can [create your own environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands), or [clone an existing environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#cloning-an-environment) and then modify it for your purposes.

## Preferred python interface
Our lab uses two different Integrated Development Environments (IDEs) or front-ends for interacting with python, and writing, running, debugging, and plotting tasks.

These two front ends are:

|**Spyder**|**Jupyter Lab**|
| -- | -- |
| You can open this program by typing `spyder` at the terminal or Anaconda Prompt window. | Jupyter Lab runs in a web browser window and you can open it by typing `jupyter lab` at the terminal or Anaconda Prompt.|
| Spyder is generally a little better for writing complete, autonomous scripts, and writing out more complicated computing workflows. Spyder is very similar to the Matlab user interface. | Jupyter Lab is potentially more useful for data exploration, and it allows text and figures to be stored right with the code. If you're just getting started, _Tim recommends trying Jupyter Lab._ |
| A traditional IDE, used by developers to write functions and scripts. | Rapidly growing development environment, on the ascendency for data scientists, with expanding popularity and functionality. |
| Used to write .py files, although py files can work with Jupyter. | Used to write .ipynb files, although these files can be exported as py files. |
| Produces python code that is potentially more portable, and easier to share with python beginners. | Produces python code with more formatting, bells and whistles, and self-contained because of embedded figures and text. |
| <img src="../images/spyder.png" alt="Spyder screenshot" width="400"/> | <img src="../images/jupyter.png" alt="Jupyter screenshot" width="400"/> |

