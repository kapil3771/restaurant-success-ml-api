from fastapi import FastAPI
import numpy as np
from app.schemas import RestaurantInput, PredictionResponse
from app.model import load_models, predict

app = FastAPI(
    title="Restaurant Success ML API",
    version="1.0.0"
)

@app.on_event("startup")
def startup_event():
    load_models()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictionResponse)
def predict_restaurant(data: RestaurantInput):
    features = np.array([[
        data.location,
        data.rest_type,
        data.cuisines,
        data.book_table,
        data.votes
    ]])

    success, cost = predict(features)

    return {
        "success_prediction": success,
        "estimated_cost_for_two": cost
    }