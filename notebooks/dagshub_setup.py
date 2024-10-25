import dagshub
import mlflow
dagshub.init(repo_owner='prashantmalik3008', repo_name='youtube_comment_analysis', mlflow=True)

mlflow.set_tracking_uri("https://dagshub.com/prashantmalik3008/youtube_comment_analysis.mlflow")
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)