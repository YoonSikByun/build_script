FROM ghcr.io/mlflow/mlflow:v2.13.2

RUN apt-get update && apt-get install -y procps && \
         apt-get install vim -y && \
         apt-get install -y gcc libpq-dev && \
         pip install psycopg2==2.9.9 && \
         mkdir -p /opt/mlflow/mlruns && \
         mkdir -p /opt/mlflow/.mlflow