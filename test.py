import mlflow
from mlflow.tracking import MlflowClient

MIN_ACCURACY = 0.90

mlflow.set_tracking_uri("./mlruns")
#mlflow.set_tracking_uri("http://localhost:5000")

client = MlflowClient()
experiment = client.get_experiment_by_name("jenkins Classifier Experiment1")

runs = client.search_runs(
    experiment_ids=[experiment.experiment_id],
    order_by=["start_time DESC"],
    max_results=1,
)

run = runs[0]
accuracy = run.data.metrics.get("eval_accuracy")

print(f"Model accuracy: {accuracy}")

if accuracy < MIN_ACCURACY:
    raise Exception(
        f"Model accuracy {accuracy} below threshold {MIN_ACCURACY}"
    )

print("✅ Model passed quality gate")
