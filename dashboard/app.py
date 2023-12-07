# app.py
import dash_daq as daq
import pandas as pd
from dash import Dash, Input, Output, dcc, html, State
from datetime import datetime
import plotly.express as px
import requests
import json
import dash
import dash_bootstrap_components as dbc
import plotly.graph_objs as go


API_URL = 'http://127.0.0.1:8000/'
PREDICTION_ENDPOINT = 'job_prediction'
RECOMMENDATION_ENDPOINT = 'skills_recommendation'
GET_JOBS = 'get_jobs'
DATA_PATH = '../data/processed/data_engineered_df.pkl'

df = pd.read_pickle(DATA_PATH)
level_0_columns = [column for column in df.columns.levels[0] if column not in ['DevType', 'skills_clusters']]


external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME])
app.title = "Tech Job That Matches Me"

def generate_skills_checklist():
    check_list  = []
    for skill_type in level_0_columns:
        skills = df[skill_type].columns.tolist()
    
        group = dbc.AccordionItem(
                [
                    html.Div(
                    dcc.Checklist(
                        id=skill_type,
                        className="checklist_control",
                        options=skills,
                        inline=True,
                    )),
                ], 

                title=skill_type,
                className="accordion-item")
        
        check_list.append(group)

    return html.Div(
    dbc.Accordion(children=check_list, className="accordion-container"))

def generate_skills_summary():
    selected_skills  = []
    for skill_type in level_0_columns:
        summary =html.Div(
            children=[
                html.P(children=f"Selected {skill_type}: ", className="skill-title"),
                html.P(
                    children=(
                        "No skills selected"),
                    className="skill-group",
                id=f"{skill_type}-skills-summary"),
            ],

        )
        
        selected_skills.append(summary)

    return html.Div(className="skills-container",

     children=selected_skills)


header = html.Div(
            children=[
                html.P(children="</>", className="header-emoji", style={'font-size': '50px', 'color': 'white'}),
                html.H1(children="Tech Job That Matches Me", className="header-title"),
                html.P(
                    children=(
                        "Predict the tech job that is the best fit for you based "
                        "on your skills (programming languages, databases, platforms, frameworks, etc.)"
                    ),
                    className="header-description",
                ),
            ],
            className="header",
        )


prediction_button = html.Div(

             [
                    html.Button('Predict Jobs',
                                id='predict-button',
                                n_clicks=None,
                                className='Button'),
                ],

)

recommendation_button = html.Div(
                     html.Button('Recommend Skills',
                                id='recommend-button',
                                n_clicks=None,
                                className='Button'),)

all_jobs = requests.get(API_URL+GET_JOBS).json()

app.layout = html.Div(
    children=[header, 
    html.Div(children=generate_skills_checklist(), id="checklist-input",),
    html.Div(children=[generate_skills_summary()]),
       #start of dropdown
    html.Div(className="buttons-container", children=[
        prediction_button,
        html.Br(),
        html.P("     or    Select a job to get skills recommendations:", style={'font-weight': 'bold'}),
        dcc.Dropdown(id="job-selector",
                            options = [
                                {
                                    "label": job,
                                    "value": job,
                                            }
                                            for job in all_jobs['jobs']
                                     ],
                            clearable=True,
                            placeholder="Select a job",
                            className="dropdown",
                        ),
                        recommendation_button], ),#end of dropdown

    dbc.Spinner(color="primary", children=html.Div(children=[], id="job-section")),

    dbc.Spinner(color="primary", children=html.Div(children=[], id="skill-recommender")),

 
           ]        )
                            

for skill_type in level_0_columns:
    @app.callback(
        Output(component_id=f"{skill_type}-skills-summary", component_property='children'),
        Input(component_id=skill_type, component_property='value')
    )
    def skills_summary(skills):
        try:
            return html.Ul([html.Li(skill) for skill in skills])

        except:
            return "No skills selected"
    

@app.callback(
    Output(component_id='job-section',component_property= 'children'),

    inputs=dict(n_clicks=Input('predict-button', 'n_clicks')),
    state=dict(lang=State(level_0_columns[0], 'value'),
    db =State(level_0_columns[1], 'value'),
    platforms =State(level_0_columns[2], 'value'),
    webframeworks =State(level_0_columns[3], 'value'),
    mistech =State(level_0_columns[4], 'value'),
    dev_tools =State(level_0_columns[5], 'value'))
)
def predict_job(n_clicks, lang, db, platforms, webframeworks, mistech, dev_tools):
    if n_clicks is not None:
        input_data = {
            'available_skills': [skill for skill_list in [lang, db, platforms, webframeworks, mistech, dev_tools] if skill_list for skill in skill_list]
        }
        response = requests.post(API_URL+PREDICTION_ENDPOINT, json=input_data)
        if response.status_code == 200:
            json_obj = json.loads(response.json()['predicted_jobs'])
            # Reverse the order of the first 15 matched jobs
            reversed_keys = list(json_obj.keys())[:15][::-1]
            reversed_values = list(json_obj.values())[:15][::-1]
            # Create the horizontal bar chart
            trace = go.Bar(
                x=reversed_values,
                y=reversed_keys,
                orientation='h'
            )
            layout = go.Layout(
                                title='Most probable jobs',
                                xaxis=dict(title='% of matching'),
                                yaxis=dict(title='Job title'),
                            )
            fig = go.Figure(data=[trace], layout=layout)

            return dcc.Graph(figure=fig, style={'margin-top: ':'90px', 'margin-bottom': '50px'})
        else:
            return html.P(children="Error in the API call", style={'color': 'red'})
    return dash.no_update


@app.callback(
    Output(component_id='skill-recommender', component_property='children'),


    inputs=dict(n_clicks=Input('recommend-button', 'n_clicks')),
    state=dict(lang=State(level_0_columns[0], 'value'),
    db =State(level_0_columns[1], 'value'),
    platforms =State(level_0_columns[2], 'value'),
    webframeworks =State(level_0_columns[3], 'value'),
    mistech =State(level_0_columns[4], 'value'),
    dev_tools =State(level_0_columns[5], 'value'),
    target_job = State('job-selector', 'value')),
)
def recommend_skill(n_clicks, lang, db, platforms, webframeworks, mistech, dev_tools, target_job):
    if n_clicks is not None:
        input_data = {
            'available_skills': [skill for skill_list in [lang, db, platforms, webframeworks, mistech, dev_tools] if skill_list for skill in skill_list],
            'target_job': target_job,
            'threshold': -10
        }
        response = requests.post(API_URL+RECOMMENDATION_ENDPOINT, json=input_data)

        if response.status_code == 200:
            json_obj = json.loads(response.json()['new_skills'])
            # Reverse the order of the first 15 matched jobs
            reversed_keys = list(json_obj.keys())[:15][::-1]
            reversed_values = list(json_obj.values())[:15][::-1]
            # Create the horizontal bar chart
            trace = go.Bar(
                x=reversed_values,
                y=reversed_keys,
                orientation='h',
                marker=dict(color='rgb(49,130,189)')
            )
            layout = go.Layout(
                                title='Most recommended skills',
                                xaxis=dict(title='% of relevance'),
                                yaxis=dict(title='skill'),
                            )
            fig = go.Figure(data=[trace], layout=layout)

            return dcc.Graph(figure=fig, style={'margin-bottom': '50px',})
        else:
            return html.P(children="Error in the API call", style={'color': 'red'})
    return dash.no_update

if __name__ == "__main__":
    app.run_server(debug=True)
                            