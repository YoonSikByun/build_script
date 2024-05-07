docker build --no-cache -t mlstudio/ubi8.9:latest -f ./Dockerfile-ubi8.9 .
docker rmi $(docker images --filter "dangling=true" -q --no-trunc)