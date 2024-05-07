from datetime import datetime, timedelta
from textwrap import dedent
from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator

from kubernetes import client as k8s

etl_image = "path_to_a_super_secret_image"

volume_mounts = [
    k8s.V1VolumeMount(name="dag-storage", mount_path='/data', sub_path=None, read_only=False),
    k8s.V1VolumeMount(name="mlstudio-global-config", mount_path='/data', sub_path=None, read_only=False)
]

volumes = [
    k8s.V1Volume(
        name='dag-storage',
        persistent_volume_claim=k8s.V1PersistentVolumeClaimVolumeSource(claim_name='dag-storage')
    ),
    k8s.V1Volume(name='mlstudio-global-config', config_map=k8s.V1ConfigMapVolumeSource(name='test'))
]

# [START default_args]
default_args = {
    'owner': 'admin',
    'depends_on_past': False,
    'email': ['admin@email.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}
# [END default_args]

# [START instantiate_dag]
with DAG(
    'pipeline-c6YdSiZ7jZJmWYv1OWY18',
    default_args=default_args,
    description='',
    schedule_interval='@once',
    start_date=datetime(2024, 5, 1),
    catchup=False,
    tags=['admin', 'run_alll', 'project-NbUNpF5qp63vWvATg7Fs7', 'pipeline-c6YdSiZ7jZJmWYv1OWY18'],
    is_paused_upon_creation=False
) as dag:
    # [END instantiate_dag]

    # [START tasks]
    k = KubernetesPodOperator(
        name="hello-dry-run",
        namespace='mlstudio',
        image="debian",
        cmds=["bash", "-cx"],
        arguments=["echo", "10"],
        labels={"foo": "bar"},
        task_id="dry_run_demo",
        volumes=volumes,
        volume_mounts=volume_mounts,
        do_xcom_push=True,
    )
    # [END tasks]

    # [START task pipe lines]
    k
    # [END task pipe lines]

# [END tutorial]