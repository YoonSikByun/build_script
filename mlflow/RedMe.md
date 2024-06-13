docker pull ghcr.io/mlflow/mlflow

#윈도우 Docker desktop에서 실행하는 방법
docker run -p 5000:5000 --name mlflow-server -v /run/desktop/mnt/host/e/mnt/mlflow:/mlflow ghcr.io/mlflow/mlflow:latest mlflow server --host 0.0.0.0

docker run -p 5000:5000 --name mlflow-server -v /run/desktop/mnt/host/e/mnt/mlflow:/mlflow mlstudio/mlflow2.13.2:latest mlflow server --host 0.0.0.0

