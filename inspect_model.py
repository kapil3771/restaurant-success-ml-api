# inspect_model.py
import joblib

clf = joblib.load("rf_classifier.pkl")

print("Number of features:", clf.n_features_in_)
print("Feature names seen during training:")
print(clf.feature_names_in_)