from fastapi import FastAPI, HTTPException
import pandas as pd
from Schema.user_input import UserInput
from fastapi.responses import JSONResponse
from Model.predict import predict_output, MODEL_VERSION, model
from Schema.predfiction_responses import PredictionResponse

app = FastAPI()

@app.get('/')
def home():
    return "Welcome to the insurance premium prediction API"

@app.get('/health')
def health():
    return {
        'status': 'ok',
        'version': MODEL_VERSION,
        'Model_load': model is not None
    }

@app.post('/predict',response_model=PredictionResponse)
def predict_premium(data: UserInput):

    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    prediction = predict_output(user_input)

    return JSONResponse(status_code=200, content={'predicted_category': prediction})

#Now we will create a schema for the user input for Separation of concerns