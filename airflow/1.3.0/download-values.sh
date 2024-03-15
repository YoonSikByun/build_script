# helm repo add apache-airflow https://airflow.apache.org/
helm show values apache-airflow/airflow --version 1.3.0 > values.yaml