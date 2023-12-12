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

## Technologies and methodology:
    Model: Xgboost classifier
    Machine learning lifecycle organization: MLflow
    API development: Apache Flask
    Web app development: Dash Plotly


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



## Features Engineering
- Full stack and back-end developer classes represented the majority of the responses, in addition to having the potential to include sub-profiles
  (eg. backend can be a Java developer or C++ developer etc.). I decided to cluster them and extract useful sub-profiles from them to increase the specificity
  of job profiles, for this task, I used DBscan because it can deal with clusters of arbitrary shapes and densities.
- I merged scientist and researcher classes as they represent more or less the same job profile


## Model development

First I used linear regression as a base model to compare other models to it 

| Model     	                | Recall score 	    |
|-------------------	        |------------------	|
| Linear regression          	| 37% 	            |
| Random forest     	        | 82% 	            |
| Xgboost               	    | 82% 	            |


Why recall score?
Because it was more important for me the percentage of detecting the job right than having false positive results.

Xgboost and Random Forest gave nearly equal performance but I chose Xgboost as it is smaller in size compared to Random Forest, which was around 9GB of size.


## Limitations and what can be improved
- Hyperparameter tuning with grid search or random search.
- More feature engineering and statistical analysis.

## Explore the notebook
To explore the notebook [here](https://github.com/aya9aladdin/used-cars-price-prediction/tree/main/notebooks)

## APP Demo

https://youtu.be/up6f-HBg1H0?si=zrbtpbfAM3XoDJLm
