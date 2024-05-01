- source : https://github.com/kubernetes-sigs/nfs-subdir-external-provisioner

helm repo add nfs-subdir-external-provisioner https://kubernetes-sigs.github.io/nfs-subdir-external-provisioner/
helm install nfs-subdir-external-provisioner nfs-subdir-external-provisioner/nfs-subdir-external-provisioner --set nfs.server=x.x.x.x --set nfs.path=/exported/path

helm show values nfs-subdir-external-provisioner/nfs-subdir-external-provisioner > values.yaml
helm template nfs-subdir-external-provisioner -f values.yaml nfs-subdir-external-provisioner/nfs-subdir-external-provisioner \
    --set nfs.server=10.1.4.240 \
    --set nfs.path=/exports > nfs-subdir-external-provisioner.yaml

- example yaml : https://github.com/kubernetes-sigs/nfs-subdir-external-provisioner/tree/master/deploy

- test

kubectl create -f https://raw.githubusercontent.com/kubernetes-sigs/nfs-subdir-external-provisioner/master/deploy/test-claim.yaml -f https://raw.githubusercontent.com/kubernetes-sigs/nfs-subdir-external-provisioner/master/deploy/test-pod.yaml

kubectl delete -f https://raw.githubusercontent.com/kubernetes-sigs/nfs-subdir-external-provisioner/master/deploy/test-claim.yaml -f https://raw.githubusercontent.com/kubernetes-sigs/nfs-subdir-external-provisioner/master/deploy/test-pod.yaml


helm install nfs-client-provisioner --set nfs.server=172.30.1.13 --set nfs.path=/Users/yoonsikbyun/Documents/exports stable/nfs-client-provisioner