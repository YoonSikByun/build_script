from datetime import datetime, timedelta
from textwrap import dedent
from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator

from kubernetes import client as k8s

etl_image = "path_to_a_super_secret_image"

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
        image="",
        cmds=["bash", "-cx"],
        arguments=["echo", "10"],
        labels={"foo": "bar"},
        task_id="dry_run_demo",
        do_xcom_push=True,
    )
    # [END tasks]

    # [START task pipe lines]
    k
    # [END task pipe lines]

# [END tutorial]