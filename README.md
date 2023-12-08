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

This project aims to simplify career decisions in the tech industry by creating a user-friendly platform that predicts the essential skills for specific jobs plus  recommending jobs based on an individual's current skill set. Using supervised classification and machine learning, the system will analyze job descriptions to provide accurate skill predictions and offer personalized job matches.

