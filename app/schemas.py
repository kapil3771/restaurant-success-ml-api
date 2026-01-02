from pydantic import BaseModel

class RestaurantInput(BaseModel):
    location: int
    rest_type: int
    cuisines: int
    book_table: int
    votes: int

class PredictionResponse(BaseModel):
    success_prediction: int
    estimated_cost_for_two: int