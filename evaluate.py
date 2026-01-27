import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

mlflow.set_tracking_uri("./mlruns")
#mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("jenkins Classifier Experiment")

# Load data
data = load_iris(as_frame=True)
X, y = data.frame.iloc[:, :-1], data.frame.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Get latest run
client = mlflow.tracking.MlflowClient()
experiment = client.get_experiment_by_name("jenkins Classifier Experiment")

runs = client.search_runs(
    experiment_ids=[experiment.experiment_id],
    order_by=["start_time DESC"],
    max_results=1,
)

run_id = runs[0].info.run_id

# Load model
model_uri = f"runs:/{run_id}/random_forest_model"
model = mlflow.sklearn.load_model(model_uri)

# Evaluate
accuracy = model.score(X_test, y_test)

mlflow.start_run(run_id=run_id)
mlflow.log_metric("eval_accuracy", accuracy)
mlflow.end_run()

print(f"Evaluation accuracy: {accuracy}")
