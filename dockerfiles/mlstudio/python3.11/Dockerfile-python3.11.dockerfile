# This image provides a Python 3.11 environment you can use to run your Python
# applications.
FROM mlstudio/ubi8.9:latest

RUN INSTALL_PKGS="python3.11 python3.11-devel python3.11-setuptools python3.11-pip nss_wrapper \
        httpd httpd-devel mod_ssl mod_auth_gssapi mod_ldap \
        mod_session atlas-devel gcc-gfortran libffi-devel libtool-ltdl \
        enchant krb5-devel" && \
    yum -y module enable  httpd:2.4 && \
    yum -y --setopt=tsflags=nodocs install $INSTALL_PKGS && \
    rpm -V $INSTALL_PKGS && \
    # Remove redhat-logos-httpd (httpd dependency) to keep image size smaller.
    rpm -e --nodeps redhat-logos-httpd && \
    yum -y clean all --enablerepo='*'

# Set the default CMD to print the usage of the language image.
CMD $STI_SCRIPTS_PATH/usage