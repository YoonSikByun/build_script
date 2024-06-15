# docker run -p 5050:5000 --name mlflow-server -v /Users/yoonsikbyun/Documents/minikube_mnt/mlflow:/mlflow mlstudio/mlflow2.13.2:latest mlflow server --host 0.0.0.0
docker run -p 5050:5000 --name mlflow-server \
    -e MLFLOW_REGISTRY_URI='postgresql://mlflow:mlflow@192.168.64.1:30000/mlflow' \
    -e MLFLOW_TRACKING_URI='postgresql://mlflow:mlflow@192.168.64.1:30000/mlflow' \
    -e MLFLOW_AUTH_CONFIG_PATH='/mlflow/config/basic_auth.ini' \
    -v /Users/yoonsikbyun/Documents/minikube_mnt/mlflow/mlruns:/opt/mlflow \
    mlstudio/mlflow2.13.2:latest \
    mlflow \
    server \
    --app-name basic-auth \
    --host 0.0.0.0 \
    --backend-store-uri postgresql://mlflow:mlflow@192.168.64.1:30000/mlflow \
    --default-artifact-root file:/opt/mlflow/mlruns

    # --default-artifact-root file:/Users/yoonsikbyun/Documents/minikube_mnt/mlruns
