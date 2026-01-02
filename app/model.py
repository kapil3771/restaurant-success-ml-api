import joblib
import pandas as pd

classifier = None
regressor = None

FEATURE_COLUMNS = [
    "location",
    "rest_type",
    "cuisines",
    "book_table",
    "votes"
]

def load_models():
    global classifier, regressor
    classifier = joblib.load("rf_classifier.pkl")
    regressor = joblib.load("rf_regressor.pkl")

def predict(features):
    df = pd.DataFrame(features, columns=FEATURE_COLUMNS)

    success = int(classifier.predict(df)[0])
    cost = int(regressor.predict(df)[0])

    return success, cost