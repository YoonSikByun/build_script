kubectl delete pv <pv_name> --grace-period=0 --force
kubectl patch pv <pv_name> -p '{"metadata": {"finalizers": null}}'

kubectl patch pv <pv_name> -p '{\"metadata\": {\"finalizers\": null}}' # <== 윈도우에서는 큰따옴표 앞에 \ 을 붙여야된다.

kubectl delete pvc <pvc_name> --grace-period=0 --force
kubectl patch pvc <pvc_name> -p '{"metadata": {"finalizers": null}}'

kubectl delete pvc data-apache-airflow-postgresql-0 --grace-period=0 --force
kubectl patch pvc data-apache-airflow-postgresql-0 -p '{"metadata": {"finalizers": null}}'


kubectl delete pvc pvc-host-nfs --grace-period=0 --force
kubectl patch pvc pvc-host-nfs -p '{"metadata": {"finalizers": null}}'

kubectl delete pvc pvc-host-nfs --grace-period=0 --force
kubectl patch pvc pvc-host-nfs -p '{"metadata": {"finalizers": null}}'

kubectl delete pv pv-host-nfs --grace-period=0 --force
kubectl patch pv pv-host-nfs -p '{"metadata": {"finalizers": null}}'