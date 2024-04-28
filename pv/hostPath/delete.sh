kubectl delete pv <pv_name> --grace-period=0 --force
kubectl patch pv <pv_name> -p '{"metadata": {"finalizers": null}}'

kubectl delete pvc <pvc_name> --grace-period=0 --force
kubectl patch pvc <pvc_name> -p '{"metadata": {"finalizers": null}}'



kubectl delete pvc data-apache-airflow-postgresql-0 --grace-period=0 --force
kubectl patch pvc data-apache-airflow-postgresql-0 -p '{"metadata": {"finalizers": null}}'
