rm sftp-server.yaml
helm template sftp-server -f values.yaml emberstack/sftp --version 5.1.69 > sftp-server.yaml