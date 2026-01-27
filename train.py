
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

#mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_tracking_uri("./mlruns")
mlflow.set_experiment("jenkins Classifier Experiment1")

with mlflow.start_run() as run:
    # Load data
    data = load_iris(as_frame=True)
    X, y = data.frame.iloc[:, :-1], data.frame.iloc[:, -1]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)

    # Log params
    mlflow.log_param("n_estimators", 100)

    # Evaluate
    accuracy = rf.score(X_test, y_test)
    mlflow.log_metric("accuracy", accuracy)

    # Log model
    mlflow.sklearn.log_model(sk_model=rf, name="random_forest_model")

    print(f"Training accuracy: {accuracy}")
    print(f"Run ID: {run.info.run_id}")
