# 쿠버네티스에 Airflow 설치

## 참고 사이트

- https://zerohertz.github.io/k8s-airflow/
- https://airflow.apache.org/docs/helm-chart/1.3.0/index.html

## 필요 사항

- 쿠버네티스 v1.19에서는 airflow helm chart 1.3.0 이하부터 사용 가능

## 설치 방법

- Repository 추가
    
    > helm repo add apache-airflow https://airflow.apache.org/
    > 
1. Chart 설치
    1. 공통
        - values.yaml 다운로드
            
            > helm show values apache-airflow/airflow --version 1.3.0 > values.yaml
            > 
        - values.yaml 다운로드
            
            > helm show values apache-airflow/airflow --version 1.3.0 > values.yaml
            > 
    2. OnPremise
        - 설치 yaml 생성
            
            > helm template apache-airflow -f values.yaml apache-airflow/airflow --version 1.3.0 > airflow-1.3.0.yaml
            > 
    3. On-line
        
        > helm install airflow apache-airflow/airflow --version 1.3.0 -f values.yaml -n airflow —create-namespace
        >