import os
import joblib
import pandas as pd

# Environment-driven model location
MODEL_DIR = os.getenv("MODEL_DIR", "/models")

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

    classifier_path = os.path.join(MODEL_DIR, "rf_classifier.pkl")
    regressor_path = os.path.join(MODEL_DIR, "rf_regressor.pkl")

    if not os.path.exists(classifier_path) or not os.path.exists(regressor_path):
        raise FileNotFoundError(
            f"Model files not found in {MODEL_DIR}"
        )

    classifier = joblib.load(classifier_path)
    regressor = joblib.load(regressor_path)

def predict(features):
    if classifier is None or regressor is None:
        raise RuntimeError("Models are not loaded. Call load_models() first.")

    df = pd.DataFrame(features, columns=FEATURE_COLUMNS)

    success = int(classifier.predict(df)[0])
    cost = int(regressor.predict(df)[0])

    return success, cost