docker build --no-cache -t mlstudio/jupyterlab-extenstions4.1.8:latest -f ./Dockerfile-jupyterlab4.1.8-extensions .
docker rmi $(docker images --filter “dangling=true” -q --no-trunc)