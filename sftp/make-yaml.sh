rm sftp-server.yaml
# helm template mlflow -f values.yaml community-charts/mlflow  --version 0.7.19 > mlflow-0.7.19.yaml
helm template sftp-server -f values.yaml emberstack/sftp --version 5.1.69 > sftp-server.yaml