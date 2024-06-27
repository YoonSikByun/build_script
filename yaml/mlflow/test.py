http://localhost:32050/#/experiments/0?searchFilter=&orderByKey=attributes.start_time&orderByAsc=false&startTime=ALL&lifecycleFilter=Active&modelVersionFilter=All+Runs&datasetsFilter=W10%3D

http://localhost:32050/#/experiments/0

http://admin:admin@localhost:32050/ajax-api/2.0/mlflow/experiments/search?max_results=20000

http://admin:admin@localhost:30002/mlflow/ajax-api/2.0/mlflow/experiments/search?max_results=20000

http://admin:admin@localhost:32050/ajax-api/2.0/mlflow/experiments/get?experiment_id=0


http://admin:admin@localhost:32050/ajax-api/2.0/mlflow/runs/search

http://localhost:32050/ajax-api/2.0/mlflow/runs/search


http://admin:admin@localhost:30002/mlflow

http://admin:admin@localhost:30002/mlflow-ui/


vi /usr/local/lib/python3.10/site-packages/mlflow/server/auth/__init__.py

http://localhost:30002/mlflow?login_username=admin&login_password=admin


import logging
import base64
logging.basicConfig(filename='/opt/mlflow/.mlruns/mlflow.log', level=logging.DEBUG)

def authenticate_request_basic_auth() -> Union[Authorization, Response]:
    """Authenticate the request using basic auth."""
    username = ''
    password = ''

    logging.debug(f'request.authorization : {request.authorization}')
    logging.debug(f'type(request.authorization) : {type(request.authorization)}')

    if request.authorization is None:
        username = request.args.get('login_username')
        password = request.args.get('login_password')
        logging.debug(f'-------- username : [{username}]')
        logging.debug(f'-------- password : [{password}]')
        if not username and not password:
            return make_basic_auth_response()

        if store.authenticate_user(username, password):
            token = f'{username}:{password}'
            logging.debug(f'----- token : {token}')
            # token = base64.encodebytes(b"This has base64 padding").decode("utf-8").strip()
            token = bytes(token, 'utf-8')
            token = base64.encodebytes(token).decode("utf-8")
            auth = Authorization.from_header(f"Basic {token}")
            logging.debug(f'type(auth) : {type(auth)}')
            logging.debug(f'auth : {auth}')
            logging.debug(f'auth.username : {auth.username}')
            logging.debug(f'auth.password : {auth.password}')
            #return 'Basic YWRtaW46YWRtaW4='
            request.authorization = auth
            return auth
        else:
            # let user attempt login again
            return make_basic_auth_response()

    username = request.authorization.username
    password = request.authorization.password

    if store.authenticate_user(username, password):
        return request.authorization
    else:
        # let user attempt login again
        return make_basic_auth_response()
