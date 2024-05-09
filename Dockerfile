FROM python:alpine3.19
USER root
RUN adduser -s /bin/ash -h /home/oliver -D oliver
USER oliver
WORKDIR /home/oliver
RUN pip install pytest
ENTRYPOINT export PATH="/home/oliver/.local/bin:$PATH" && ash
