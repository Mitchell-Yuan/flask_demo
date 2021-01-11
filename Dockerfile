FROM python:3.7.8-slim-buster

LABEL app.maintainer=mitchell
LABEL app.version="1.0"

RUN git clone https://github.com/Mitchell-Yuan/flask_demo.git

RUN apt-get update && apt-get install -y --no-install-recommends tzdata  && rm -rf /var/lib/apt/lists/*
ENV TZ Asia/Shanghai

RUN apt-get install --assume-yes apt-utils

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \
    nginx \
    vim

EXPOSE 80 5000 

RUN chmod +x /flask-rest/start.sh; \
    pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com --upgrade pip ; \
    pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com -r /flask-rest/requirements.txt ;
