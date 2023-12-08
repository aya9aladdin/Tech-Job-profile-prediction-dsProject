import pandas as pd 
import numpy as np
import pickle
from mlflow.tracking import MlflowClient
from matplotlib import pyplot as plt
import json

LOG_DATA_PKL    =  "/data/data_details"
LOG_MODEL_PKL   =  "/model/model.pkl"

class JobPrediction:
    """Production Class for predicting the probability of a job from skills"""

    # Constructor
    def __init__(self, mlflow_tracking_uri, run_id):

        client = MlflowClient(mlflow_tracking_uri)
        run = client.get_run(run_id)
        artificats_path = run.info.artifact_uri
        model_artifact_path = artificats_path + LOG_MODEL_PKL
        data_artifact_uri = artificats_path + LOG_DATA_PKL

        # Load the pipeline from the pickle file
        with open(model_artifact_path, 'rb') as file:
            self.classifier = pickle.load(file)

        with open(data_artifact_uri, "r") as file:
            self.data = json.load(file)


    # ========================================================
    # ***********           Getters               ************
    # ========================================================

    def get_all_skills(self):
        return self.data['features_names']

    def get_all_jobs(self):
        return self.data['targets_names']
    

    # ========================================================
    # **************    Prediction Functions    **************  
    # ========================================================
    
    
    def predict_jobs_probabilities(self, available_skills):
        '''Returns probabilities of the different jobs according to the skills'''
        # Create features array 
        features = pd.DataFrame(data=np.zeros((1, len(self.data['features_names']))), columns=self.data['features_names'],
                                dtype=int)

        target = pd.DataFrame(data=np.zeros((1, len(self.data['targets_names']))), columns=self.data['targets_names'], dtype=int)
        
        if any(skill not in self.data['features_names'] for skill in available_skills) or len(available_skills) == 0:
            raise ValueError(f"invalid skill name: {available_skills}")
        
        features[available_skills] = 1

        prediction = self.classifier.predict_proba(features.values)
        target.iloc[0] = prediction[0] * 100

        return target.iloc[0].sort_values(ascending=False).to_json()


    # ========================================================
    # **************    Simulation Functions    **************
    # ========================================================

    def recommend_new_skills(self, available_skills, target_job, threshold=0):
        # Calculate base probability
      
        if any(skill not in self.data['features_names'] for skill in available_skills) or len(available_skills) == 0:
            raise ValueError(f"invalid skill name: {available_skills}")
        
        if target_job not in self.data['targets_names']:
            raise ValueError(f"invalid job name: {target_job}")
        
        features = pd.DataFrame(data=np.zeros((1, len(self.data['features_names']))), columns=self.data['features_names'],
                                dtype=int)

        target = pd.DataFrame(data=np.zeros((1, len(self.data['targets_names']))), columns=self.data['targets_names'], dtype=int)
        
        features[available_skills] = 1

        prediction = self.classifier.predict_proba(features.values)
        target.iloc[0] = prediction[0] * 100
        base_prediction = target[target_job].values[0]
        target_job_index = target.columns.get_loc(target_job)
        featuers_effect = []
        new_skills = []

        skills = [skill for skill in self.data['features_names'] if skill not in available_skills]
        for skill in skills:
                new_features = features.copy()
                new_features[skill] = 1
                prediction = self.classifier.predict_proba(new_features.values)[0]

                effect = (prediction[target_job_index]*100 - base_prediction)/base_prediction
                featuers_effect.append(effect)
                new_skills.append(skill)


        featuers_effect = pd.Series(data=featuers_effect, index=new_skills)
        featuers_effect.sort_values(ascending=False, inplace=True)
        featuers_effect = featuers_effect[featuers_effect > threshold]
        return featuers_effect.to_json()

    # ==============================================================
    