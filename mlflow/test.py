http://localhost:32050/#/experiments/0?searchFilter=&orderByKey=attributes.start_time&orderByAsc=false&startTime=ALL&lifecycleFilter=Active&modelVersionFilter=All+Runs&datasetsFilter=W10%3D

http://localhost:32050/#/experiments/0

http://admin:admin@localhost:32050/ajax-api/2.0/mlflow/experiments/search?max_results=20000

http://admin:admin@localhost:30002/mlflow/ajax-api/2.0/mlflow/experiments/search?max_results=20000

http://admin:admin@localhost:32050/ajax-api/2.0/mlflow/experiments/get?experiment_id=0


http://admin:admin@localhost:32050/ajax-api/2.0/mlflow/runs/search

http://localhost:32050/ajax-api/2.0/mlflow/runs/search


http://admin:admin@localhost:30002/mlflow



/usr/local/lib/python3.10/site-packages/mlflow/server/auth



def authenticate_request_basic_auth() -> Union[Authorization, Response]:
    """Authenticate the request using basic auth."""
    username = ''
    password = ''
        
    if request.authorization is None:
        username = request.args.get('login_username')
        password = request.args.get('login_password')
        if not username and not password:
            return make_basic_auth_response()
        temp_auth = Authorization(auth_type='basic', data={'username': username, 'password' : password}, token='Basic YWRtaW46YWRtaW4=')
        if store.authenticate_user(username, password):
            return temp_auth
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
