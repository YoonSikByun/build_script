# This image provides a Python 3.11 environment you can use to run your Python
# applications.
FROM mlstudio/python3.11:latest

RUN yum install -y postgresql-libs postgresql-devel

ARG USERNAME=mlstudio
USER $USERNAME

RUN mkdir /home/$USERNAME/.jupyter
# RUN pip3 install --no-cache-dir matplotlib numpy pandas plotly scikit-learn scipy statsmodels xgboost lightgbm Flask gunicorn \
#     jupyterlab jupyterlab-git jupyter-resource-usage nbdime lckr_jupyterlab_variableinspector mlflow psycopg2 paramiko pysftp
RUN pip3 install --no-cache-dir matplotlib numpy pandas plotly scikit-learn scipy statsmodels xgboost lightgbm Flask gunicorn \
    jupyterlab jupyterlab-git==0.44.0 jupyterlab-system-monitor nbdime lckr_jupyterlab_variableinspector mlflow psycopg2 paramiko pysftp

ENV PATH="${PATH}:/home/$USERNAME/.local/bin:"

