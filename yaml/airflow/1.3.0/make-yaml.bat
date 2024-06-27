del airflow-1.3.0.yaml
rem helm template apache-airflow -f values.yaml apache-airflow/airflow --version 1.3.0 --namespace airflow > airflow-1.3.0.yaml
helm template apache-airflow -f values.yaml apache-airflow/airflow --version 1.3.0 > airflow-1.3.0.yaml