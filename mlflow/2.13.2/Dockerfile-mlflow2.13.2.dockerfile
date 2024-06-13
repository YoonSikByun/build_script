FROM ghcr.io/mlflow/mlflow:v2.13.2

RUN apt-get update && apt-get install -y procps && apt-get install vim -y