import json

import joblib
import uvicorn
from fastapi import FastAPI
import pandas as pd

from pydantic import BaseModel
from pydantic.config import ConfigDict


app = FastAPI(
    title="Diabetes Prediction API",
    description="API to predict the probability of a subject with given habits/traits being diabetic",
    version="1.0",
)


def load_test_input():
    with open("test_input.json", "rt", encoding="utf-8") as f_in:
        return json.load(f_in)


class PredictionOutput(BaseModel):
    """Probability of being diabetic"""

    diabetes_prob: float


class DiabetesInput(BaseModel):
    """Input object to make predictions on"""

    HighBP: int
    HighChol: int
    CholCheck: int
    BMI: int
    Smoker: int
    Stroke: int
    HeartDiseaseorAttack: int
    PhysActivity: int
    Fruits: int
    Veggies: int
    HvyAlcoholConsump: int
    AnyHealthcare: int
    NoDocbcCost: int
    GenHlth: int
    MentHlth: int
    PhysHlth: int
    DiffWalk: int
    Sex: int
    Age: int
    Education: int
    Income: int

    class Config:
        schema_extra = {"example": load_test_input()}


def load_model():
    """Load model from model.bin"""
    with open("model.bin", "rb") as f_out:
        return joblib.load(f_out)


@app.post("/predict", response_model=PredictionOutput)
def predict(features: DiabetesInput) -> PredictionOutput:
    diabetes_prob = load_model().predict_proba(pd.DataFrame([features.dict()]))[:, 1][0]
    return {"diabetes_prob": diabetes_prob}


@app.get("/healthcheck")
def healthcheck() -> dict:
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run("predict:app", reload=True)
