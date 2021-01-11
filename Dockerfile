FROM python:3.7.8-slim-buster

LABEL app.maintainer=mitchell
LABEL app.version="1.0"

# 时区设定
RUN apt-get update && apt-get install -y --no-install-recommends tzdata  && rm -rf /var/lib/apt/lists/*
ENV TZ Asia/Shanghai

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    nginx \
    vim \
    git

RUN git clone https://github.com/Mitchell-Yuan/flask_demo.git

RUN chmod +x /flask-rest/start.sh; \
    pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com --upgrade pip ; \
    pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com -r /flask-rest/requirements.txt ;

EXPOSE 80 5000 