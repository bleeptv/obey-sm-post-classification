# Overview

The aim of this project is to build a social media post classifier for the Obey application. In short, the project will generate a ML (machine learning) model that will be used to predict/estimate whether a social media post from Instagram, YouTube, Facebook, etc, is somehow related to music. 

# Requirements

In order to run this project, the following need to be installed on the local development environment:

* **Python /3.5.1** or above (**Python 3.5** and **Python 2** are **deprecated** as the time of this writing). If you are on MacOSX or Linux, Python should already come installed with the OS.
* **pip** or **conda** package managment. For this project, I'll be referring to **pip**
* **virtualenv**: Used to create a virtual python environment, so that we can download specific versions of packages needed to run the project. Install it using the following command:

```
pip install virtualenv
```

# Setting up the project
After cloning this repository, run the following command in your terminal to create a virtual environment to host the project's dependencies on your local machine:
```
virtualenv venv_1
```

**venv_1** is just name of the virtual environment I chose. Once done, enter the following command in your terminal to activate the virtual environment:
```
source venv_1/bin/activate
```

Once the environment is activated, navigate to the **project's root directory**, then run this command in the terminal:
```
pip install -r requirements.txt
```

This will install all the necessary dependencies to run the project, including the **Jupyter Lab** IDE.

# Running the Demo Notebook

Run the following command from the terminal to start the **Jupyter Lab** IDE:
```
jupyter-lab
```

In the project root folder, open the **/notebooks/topic_modelling_instagram.ipnyb** file.<br>
To run a cell block in the notebook file, press the **Shift + Enter** key (Windows) on your keyboard, or press the **play button** in the top console.