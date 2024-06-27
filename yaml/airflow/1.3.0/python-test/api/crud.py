import airflow_client.client
from airflow_client.client.api import dag_api
import traceback

api_url = 'http://localhost:5000/api/v1'
username = 'admin'
password = 'admin'

configuration = airflow_client.client.Configuration(
    host=api_url, username=username, password=password
)

# Airflow 모든 Dag를 조회한다.
def get_dags():
    success = True
    msg = 'success'
    api_response = None
    try:
        with airflow_client.client.ApiClient(configuration) as api_client:
            dag_api_instance = dag_api.DAGApi(api_client)
        
            api_response = dag_api_instance.get_dags()
    except airflow_client.client.OpenApiException as e:
        msg = f"Exception when calling DagAPI->get_dags: {e}"
        success = False
    except BaseException:
        msg = traceback.format_exc()
        success = False
        
    return {'status' : success, 'reason' : msg, 'data' : api_response}

def get_dag(dag_id):
    success = True
    msg = 'success'
    api_response = None
    try:
        with airflow_client.client.ApiClient(configuration) as api_client:
            dag_api_instance = dag_api.DAGApi(api_client)
            api_response = dag_api_instance.get_dag(dag_id=dag_id)
    except airflow_client.client.OpenApiException as e:
        msg = f"Exception when calling DagAPI->get_dags: {e}"
        success = False
    except BaseException:
        msg = traceback.format_exc()
        success = False

    return {'status' : success, 'reason' : msg, 'data' : api_response}

if __name__ == '__main__':
    # rtn = get_dags()
    rtn = get_dag(dag_id='tutorial')
    print(rtn)