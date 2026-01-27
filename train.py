import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Set up MLflow tracking URI (can be a local path, a remote server, etc.)
# If not set, it defaults to a local 'mlruns' directory
#mlflow.set_tracking_uri("./mlruns")
mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("Iris Classifier Experiment")

with mlflow.start_run():
    # Load data
    data = load_iris(as_frame=True)
    X, y = data.frame.iloc[:, :-1], data.frame.iloc[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Define and train model
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)

    # Log parameters
    mlflow.log_param("n_estimators", 100)

