

from flask import Flask
from flask_restful import Resource, Api, reqparse

from job_prediction import JobPrediction
#from flask import Flask, request, jsonify

import numpy as np
import pickle

from datetime import datetime

import pandas as pd

MLFLOW_TRACKING_URI = "../mlflow"
MLFLOW_RUN_ID = "7396a38eb17e42898bc5586415caf600"


# Initiate API and JobPrediction object
app = Flask(__name__)


api = Api(app)

prediction_obj = JobPrediction(mlflow_tracking_uri=MLFLOW_TRACKING_URI,
                          run_id=MLFLOW_RUN_ID)

class JobPrediction(Resource):
    def post(self):
        parser = reqparse.RequestParser()
 
        parser.add_argument('available_skills', type=str, action = 'append', required=True)

        args = parser.parse_args()
                
        prediction = prediction_obj.predict_jobs_probabilities(args['available_skills'])
        return {'predicted_jobs': prediction}


class SkillsRecommendation(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        arguments = [
        ('available_skills', list,
         'target_job', str),
         'threshold', int
    ]
        
        parser.add_argument('available_skills', type=str, action = 'append', required=True)
        parser.add_argument('target_job', type=str, required=True)
        parser.add_argument('threshold', type=int, required=True)

        args = parser.parse_args()
        
        prediction = prediction_obj.recommend_new_skills(args['available_skills'], args['target_job'], args['threshold'])
        return {'new_skills': prediction}

class GetJobs(Resource):
    def get(self):
        data = prediction_obj.get_all_jobs()  # Replace 'get_data()' with the actual method to retrieve data from prediction_obj
        return {'jobs': data}

api.add_resource(JobPrediction, '/job_prediction')
api.add_resource(SkillsRecommendation, '/skills_recommendation')
api.add_resource(GetJobs, '/get_jobs')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
    