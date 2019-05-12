# Model sensitivity analysis using SALib

Clinic at the [CSDMS Annual Meeting 2019](https://csdms.colorado.edu/wiki/Form:Annualmeeting2019)

## Description
Interested in which variables influence your model outcome? SALib (Sensitivity Analysis Library) provides commonly used sensitivity analysis methods implemented in a Python programming language package. In this clinic we will use these methods with example models to apportion uncertainty in model output to model variables. We will use models built with the Landlab Earth-surface dynamics framework, but the analyses can be easily adapted for other model software. No prior experience with Landlab or Python is necessary.

## Software 

Software that we will use: [Anaconda](https://www.anaconda.com), [SALib](https://salib.readthedocs.io/en/latest/), [Landlab](http://landlab.github.io/#/), and [Jupyter](https://jupyter.org).

The installation instructions below were adapted from [www.earthdatascience.org](www.earthdatascience.org).

## Anaconda installation

*under construction*

We will use the Anaconda Python 3 distribution for this clinic. Anaconda is a distribution of Python that comes with many of the scientific computing package that we will need, including Jupyter.

If you alread have Anaconda, you can skip to step XXX. If you already have Anaconda for Python 2 setup, you do not need to install Anaconda again. We will be working with Python version 3.7 in this clinic, but a Python 3.7 environment can be installed into an Anaconda 2.x distribution. We will create a conda environment with Python 3 later in these instructions.


### Windows

**IMPORTANT:** if you already have a `Python` installation on your Windows computer, the settings below will replace it with Anaconda as the default `Python`. If you have questions or concerns about this, please contact your course instructor. 

Download the <a href="https://www.anaconda.com/download/#windows" target="_blank">Anaconda installer for Windows</a>. Be sure to download the `Python` 3.7 version! 

Run the installer by double-clicking on the downloaded file and follow the steps bellow:
1. Click “Run”. 
2. Click on "Next".
3. Click on “I agree”.
4. Leave the selection on “Just me” and click on “Next”.
5. Click on "Next".
6. **Select the first option for “Add Anaconda to my PATH environment variable”** and also leave the selection on “Register Anaconda as my default Python 3.7”. Click on “Install”. 
7. When the install is complete, Click on “Next”.
8. Click on “Skip”. 
9. Click on “Finish”. 

**Test installation**

1. Search for and open the `Git Bash` program. In this `Terminal` window, type `bash` and hit enter. 
If you do not get a message back, then `Bash` is available for use. 

2. Next, type `git` and hit enter. 
If you see a list of commands that you can execute, then `Git` has been installed correctly. 

3. Next, type `conda` and hit enter.
Again, if you see a list of commands that you can execute, then Anaconda `Python` has been installed correctly.

4. Close the `Terminal` by typing `exit`.


### Mac

1. Download the installer: <a href="https://www.anaconda.com/download/" target="_blank">Anaconda installer for Mac</a>. Be sure to download the `Python` 3.x version!
2. Install: Anaconda—Double-click the .pkg file.
3. Follow the prompts on the installer screens.
4. If you are unsure about any setting, accept the defaults. You can change them later.
5. To make the changes take effect, close and then re-open your Terminal window.

**Test installation**

1. Search for and open the Terminal program (found in /Applications/Utilities).
2. Next, type `conda` and hit enter.
Again, if you see a list of commands that you can execute, then Anaconda `Python` has been installed correctly.
3. Close the `Terminal` by typing `exit`.


### Linux

1. Download the installer: <a href="https://www.anaconda.com/download/" target="_blank">Anaconda installer for Linux</a>. Be sure to download the `Python` 3.7 version!
2. In your Terminal window, run: `bash Anaconda-latest-Linux-x86_64.sh`
3. Follow the prompts on the installer screens.
4. If you are unsure about any setting, accept the defaults. You can change them later.
5. To make the changes take effect, close and then re-open your Terminal window.


**Test installation**
1. Search for and open the Terminal program. In this `Terminal` window, type `bash` and hit enter. 
If you do not get a message back, then `Bash` is available for use. 
2. Next, type `git` and hit enter. 
If you see a list of commands that you can execute, then `Git` has been installed correctly. 
3. Next, type `conda` and hit enter.
Again, if you see a list of commands that you can execute, then Anaconda `Python` has been installed correctly.
4. Close the `Terminal` by typing `exit`.
