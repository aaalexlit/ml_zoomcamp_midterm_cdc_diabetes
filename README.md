# Dataset description and attributions

The dataset used in this project is [CDC Diabetes Health Indicators](https://archive.ics.uci.edu/dataset/891/cdc+diabetes+health+indicators) originally coming from Kaggle [Diabetes Health Indicators Dataset](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset) which in turn is a modified and cleaned-up version of the [Behavioral Risk Factor Surveillance System](https://www.kaggle.com/datasets/cdc/behavioral-risk-factor-surveillance-system) dataset.  
UCI version is used for the ease of access through the use of `ucimlrepo` package.

The Diabetes Health Indicators Dataset contains healthcare statistics and lifestyle survey information about people in general along with their diagnosis of diabetes. The 35 features consist of some demographics, lab test results, and answers to survey questions for each patient. The target variable for classification is whether a patient has diabetes, is pre-diabetic, or healthy.

# Reproduce the project

## Environment setup

I prefer to use conda because it comes with a python interpreter of the specified version whereas with the other options like pipenv, poetry etc you need a base interpreter of a required version.
If you don't want to use conda, you can as well just skip the conda environment setup and use the provided Pipfile.* to reproduce the environment or just create virtual environment of your choice (eg python's built-in `venv`), and install the dependencies using the provided [requirements.txt](requirements.txt). In the latter case you need to keep in mind that the base interpreter's python version must be 3.10 and that 100% reproducibility is likely to be achieve but is not guaranteed.

Below are instructions for conda

1. Clone this repo

1. Create a clean Python 3.10 based environment and activate it
    ```shell
    conda create -n ml-zoomcamp-midterm-alex python=3.10
    conda activate ml-zoomcamp-midterm-alex
    ```

1. Install requirements
    ```shell
    pip install -r requirements.txt 
    ```

## Running the [notebook.ipynb](notebook.ipynb)

I usually run jupyter notebooks using Visual Studio Code but if it's not the IDE of your choice you can spin up a jupyter server and use your browser, using the following command

```shell
jupyter notebook
```

