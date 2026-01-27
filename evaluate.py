import joblib

joblib.dump(rf, "model.joblib")

import joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

rf = joblib.load("model.joblib")

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

score = rf.score(X_test, y_test)
print(f"Model accuracy: {score}")
   # Evaluate and log metrics
score = rf.score(X_test, y_test)
mlflow.log_metric("accuracy", score)
print(f"Model accuracy: {score}")

    # Log the model
mlflow.sklearn.log_model(rf, "random_forest_model")
print("Model logged to MLflow")
