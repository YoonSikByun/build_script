docker build --no-cache -t mlstudio/jupyterlab4.1.8:latest -f ./Dockerfile-jupyterlab4.1.8 .
docker rmi $(docker images --filter "dangling=true" -q --no-trunc)