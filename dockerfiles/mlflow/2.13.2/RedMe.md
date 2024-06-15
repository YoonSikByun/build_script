docker pull ghcr.io/mlflow/mlflow

postgresql://johndoe:randompassword@localhost:5432/mydb?schema=public

 mlflow server \
   --backend-store-uri  mysql+pymysql://root@localhost/mlflow_tracking_database \ 
   --default-artifact-root  file:/./mlruns \
   -h 0.0.0.0 -p 5000

    host: 'localhost',
    port: 30000,
    database: 'postgres',
    user: 'postgres',
    password: 'postgres',

postgresql://mlflow:mlflow@127.0.0.1:30000/mlflow

mlflow ui --backend-store-uri postgresql+psycopg2://username:password@IP:port/DBname.

# 윈도우 Docker desktop에서 실행하는 방법
docker run -p 5050:5000 --name mlflow-server -v /run/desktop/mnt/host/e/mnt/mlflow:/mlflow ghcr.io/mlflow/mlflow:latest mlflow server --host 0.0.0.0

# Mac
docker run -p 5050:5000 --name mlflow-server \
    -v /Users/yoonsikbyun/Documents/minikube_mnt/mlflow:/mlflow \
    mlstudio/mlflow2.13.2:latest \
    mlflow server --host 0.0.0.0 --backend-store-uri postgresql://mlflow:mlflow!@127.0.0.1:30000/mlflow \
                --default-artifact-root  file:/./mlruns
