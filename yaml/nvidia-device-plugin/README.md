helm repo add nvdp https://nvidia.github.io/k8s-device-plugin
helm repo update

# 최신버전 확인
helm search repo nvdp --devel

# value.yaml 다운로드
helm show values nvdp/nvidia-device-plugin --version 0.15.0 > values.yaml

helm template nvidia-device-plugin -f values.yaml nvdp/nvidia-device-plugin --version 0.15.0 > nvidia-device-plugin-0.15.0.yaml

helm template nvdp nvdp/nvidia-device-plugin -f values.yaml --namespace nvidia-device-plugin --create-namespace --version 0.15.0 > nvidia-device-plugin-0.15.0.yaml