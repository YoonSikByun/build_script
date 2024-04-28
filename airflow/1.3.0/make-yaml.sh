# rm airflow-1.3.0.yaml
rm airflow-1.3.0-airflow-2.8.0.yaml
# helm template apache-airflow -f values.yaml apache-airflow/airflow --version 1.3.0 --namespace airflow > airflow-1.3.0.yaml
helm template apache-airflow -f values-airflow-2.8.2.yaml apache-airflow/airflow --version 1.3.0 > airflow-1.3.0-airflow-2.8.0.yaml