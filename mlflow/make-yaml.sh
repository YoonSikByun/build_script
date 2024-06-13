rm mlflow-2.13.2.yaml
# helm template mlflow -f values.yaml community-charts/mlflow  --version 0.7.19 > mlflow-0.7.19.yaml
helm template mlflow -f values.yaml  oci://registry-1.docker.io/bitnamicharts/mlflow  --version 1.4.4 > mlflow-2.13.2.yaml