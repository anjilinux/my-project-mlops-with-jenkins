   # Evaluate and log metrics
score = rf.score(X_test, y_test)
mlflow.log_metric("accuracy", score)
print(f"Model accuracy: {score}")

    # Log the model
mlflow.sklearn.log_model(rf, "random_forest_model")
print("Model logged to MLflow")
