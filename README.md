# Model sensitivity analysis using SALib

Clinic at [CSDMS Annual Meeting 2019](https://csdms.colorado.edu/wiki/Form:Annualmeeting2019)

## Description
Interested in which variables influence your model outcome? SALib (Sensitivity Analysis Library) provides commonly used sensitivity analysis methods implemented in a Python programming language package. In this clinic we will use these methods with example models to apportion uncertainty in model output to model variables. We will use models built with the Landlab Earth-surface dynamics framework, but the analyses can be easily adapted for other model software. No prior experience with Landlab or Python is necessary.

## Software 

Software that we will use includes [Anaconda](https://www.anaconda.com), [SALib](https://salib.readthedocs.io/en/latest/), [Landlab](http://landlab.github.io/#/), and [Jupyter](https://jupyter.org). The installation instructions below were adapted from [www.earthdatascience.org](www.earthdatascience.org).

## Clinic repository direct download

[https://github.com/nathanlyons/sensitivity_analysis_clinic_CSDMS_2019/archive/master.zip](https://github.com/nathanlyons/sensitivity_analysis_clinic_CSDMS_2019/archive/master.zip)

## Anaconda installation

We will use the Anaconda Python 3 distribution for this clinic. Anaconda is a distribution of Python that comes with many of the scientific computing packages that we will need, including Jupyter.

If you alread have Anaconda, you can skip to the [Update Conda](## Update Conda) section. If you already have Anaconda for Python 2 setup, you do not need to install Anaconda again. We will be working with Python version 3.7 in this clinic, but a Python 3.7 environment can be installed into an Anaconda 2.x distribution. We will create a conda environment with Python 3 later in these instructions.


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

1. Search for and open the `Anaconda Prompt` program. 
2. Next, type `conda` and hit enter. If you see a list of commands that you can execute, then Anaconda `Python` has been installed correctly.
4. Close the `Terminal` by typing `exit`.


### Mac

1. Download the installer: <a href="https://www.anaconda.com/download/" target="_blank">Anaconda installer for Mac</a>. Be sure to download the `Python` 3.x version!
2. Install: Anaconda—Double-click the .pkg file.
3. Follow the prompts on the installer screens.
4. If you are unsure about any setting, accept the defaults. You can change them later.
5. To make the changes take effect, close and then re-open your Terminal window.

**Test installation**

1. Search for and open the Terminal program (found in /Applications/Utilities).
2. Next, type `conda` and hit enter. If you see a list of commands that you can execute, then Anaconda `Python` has been installed correctly.
3. Close the `Terminal` by typing `exit`.


### Linux

1. Download the installer: <a href="https://www.anaconda.com/download/" target="_blank">Anaconda installer for Linux</a>. Be sure to download the `Python` 3.7 version!
2. In your Terminal window, run: `bash Anaconda-latest-Linux-x86_64.sh`
3. Follow the prompts on the installer screens.
4. If you are unsure about any setting, accept the defaults. You can change them later.
5. To make the changes take effect, close and then re-open your Terminal window.

**Test installation**
1. Search for and open the Terminal program.
2. Next, type `conda` and hit enter. If you see a list of commands that you can execute, then Anaconda `Python` has been installed correctly.
4. Close the `Terminal` by typing `exit`.


## Update Conda

Update Conda itself:
```bash
conda update conda
```

And then:
```bash
conda update anaconda
```

## Create a Conda environment

Anaconda allows you to have different environments installed on your computer to access different versions of `Python` and different libraries. Sometimes libraries conflict which causes errors and packages not to work. 

To avoid conflicts, I created an environment specifically for this clinic that contains all of the packages that you will need.

For more information about conda environments check out the <a href="https://conda.io/docs/user-guide/tasks/index.html" target="_blank">conda documentation</a>.

Follow these steps to install the clinic environment: 

1. Download the environment file: [https://docs.google.com/uc?export=download&id=1KD-XJtHATu20GAMCen46RIaVwKQ4IOjn](https://docs.google.com/uc?export=download&id=1KD-XJtHATu20GAMCen46RIaVwKQ4IOjn)
2. Open the Terminal on your computer (i.e. `Anaconda Prompt` on Windows or `Terminal` on a Mac/Linux).
4. In the Terminal, navigate to the folder containing `enviroment.yml` that you downloaded in the previous step (e.g. `cd downloads`).
5. Then, type in the Terminal: `conda env create -f environment.yml`. This will only work if you run the command in the directory where you placed the environment.yml file.

Note that it takes a bit of time to run this setup, as it needs to download and install each library, and that you need to have internet access for this to run! 

Once the environment is installed, **always make sure that the sa-clinic environment is activated** before doing work for this clinic. 


### About the Conda Environment

### What is a .yaml File?

When you work with Anaconda, you can create custom lists that tell Anaconda where to install libraries from, and in what order. You can even specify a particular version. You write this list using  <a href="http://yaml.org/" target="_blank">yaml</a>(Yet Another Markup Language). This is an alternative to using `pip` to install `Python` packages.  

In previous steps, you used a custom .yaml list to install all of the `Python` libraries that you will need to complete the lessons in this course. This .yaml list is customized to install libraries from the repositories and in an order that minimizes conflicts. 


## Manage Your Conda Environment

You can have different `Python` environments on your computer. Anaconda allows you to easily jump between environments using a set of commands that you run in your terminal. 

### View a List of All Installed Conda Environments

You can see a list of all installed conda environments by typing:

```bash
conda info --env
```

### Activate a Conda Environment

**To activate an environment**, use the Terminal to navigate to your earth-analytics directory (e.g. `cd` to the directory). Then, type the following command to activate the environment (e.g. sa-clinic):

```bash
conda activate sa-clinic
``` 

<a href="https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html" target="_blank">For older installations of Anaconda (versions prior to 4.6)</a> on Mac, Linux, and Git Bash for Windows, type:

```bash
source activate sa-clinic
```

**Windows Users:** The lessons on this website assume that Windows users are using `Anaconda Prompt` as their primary terminal. If you need to activate a conda environment using the Command Prompt, you will need to use the following command: `activate sa-clinic`

Once the environment is activated, the name of the activated environment will appear in parentheses on the left side of your terminal. 

**Data Tip:**
Note that after you restart the Terminal, the sa-clinic environment is no longer active. You will need to activate the sa-clinic environment each time you start the Terminal by running the appropriate command provided above for your operating system.


### Deactivate a Conda Environment 

You can deactivate a conda environment if needed. Deactivating the environment switches you back to the default environment in the terminal session. 


#### Mac and Linux Instructions: 

```bash
Source deactivate sa-clinic
```

#### Windows Instructions 

```bash
deactivate sa-clinic

```

###  Delete a Conda Environment

If you ever want to delete an envrionment, you must first deactivate that environment and then type: 

```bash
conda env remove --name myenv
``` 

and replace `myenv` with the name of the environment that you want to remove. 

**Do not delete your root environment.** 
