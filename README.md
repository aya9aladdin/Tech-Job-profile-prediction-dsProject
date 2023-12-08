Tech Job prediction 
==============================

An end-to-end data science project for predicting the required skills needed for a specific tech job and jobs that best fit your current skills.

Project Organization
------------

    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third-party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── mlflow                  <- mlflow experiment runs.
    │   ├── experimentid        <- experiment runs with all its data.
    │   ├── runid               <- Each run has a separate folder.
    │       └── artifact        <- Run artifacts folder (models, etc.).
    │       └── metrics         <- Run metrics folder.
    │       └── param           <- Run parameters folder.
    │
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    


--------


## Motivation

This project aims to simplify career decisions in the tech industry by creating a user-friendly platform that predicts the essential skills for specific jobs plus  recommending jobs based on an individual's current skill set. The system will analyze job descriptions using supervised classification and machine learning to provide accurate skill predictions and offer personalized job matches.

## Data Source

The data source for this project was the [Stack overflow developers survey](https://survey.stackoverflow.co/2023/). This survey contains over
80K responses from people working in different tech jobs with corresponding skills in different tech areas. 

## Analytics at a glance

### response distribution across countries
![image](https://github.com/aya9aladdin/Tech-Job-profile-prediction-dsProject/assets/27581535/e7136fdc-ee07-4dd8-a035-1a30938d010a)

### Jobs frequency per country
![image](https://github.com/aya9aladdin/Tech-Job-profile-prediction-dsProject/assets/27581535/0489e27b-cebd-4123-b7e9-f76a68ac94b5)

### skills frequency of US responses (it's nearly the same for the rest of the countries)
![image](https://github.com/aya9aladdin/Tech-Job-profile-prediction-dsProject/assets/27581535/b5af6214-1c27-4ec6-8ecd-483e436d4ade)

### Heatmap showing the specificity of each skill per job type 
![image](https://github.com/aya9aladdin/Tech-Job-profile-prediction-dsProject/assets/27581535/c5106e93-80d7-4005-91cc-dc700a7e7ba4)

### Jobs correlation between each other
![image](https://github.com/aya9aladdin/Tech-Job-profile-prediction-dsProject/assets/27581535/b0cfcc89-f7fe-440a-ae13-8e9f92be619b)
