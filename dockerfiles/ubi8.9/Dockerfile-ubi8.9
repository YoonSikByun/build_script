# This image provides a Python 3.11 environment you can use to run your Python
# applications.
FROM redhat/ubi8:latest

ARG USERNAME=mlstudio
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && mkdir -p /opt/mlstudio \
    && chown $USER_GID /opt/mlstudio \
    #
    # [Optional] Add sudo support. Omit if you don't need to install software after connecting.
    && yum -y --nobest update \
    && yum install -y sudo procps-ng iputils git \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

COPY ./config/* /home/$USERNAME/
RUN chown -R $USER_GID:$USER_UID /home/$USERNAME/

RUN echo "$USERNAME:mlstudio" | chpasswd
RUN echo "root:mlstudio" | chpasswd

# Set the default CMD to print the usage of the language image.
CMD $STI_SCRIPTS_PATH/usage
