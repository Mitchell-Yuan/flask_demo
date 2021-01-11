FROM python:3.7.8-slim-buster
# FROM python:3.7.3

LABEL app.maintainer=mitchell
LABEL app.version="1.0"


RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak && \
    echo "deb http://mirrors.aliyun.com/debian/ stretch main non-free contrib" >/etc/apt/sources.list && \
    echo "deb-src http://mirrors.aliyun.com/debian/ stretch main non-free contrib" >>/etc/apt/sources.list && \
    echo "deb http://mirrors.aliyun.com/debian-security stretch/updates main" >>/etc/apt/sources.list && \
    echo "deb-src http://mirrors.aliyun.com/debian-security stretch/updates main" >>/etc/apt/sources.list && \
    echo "deb http://mirrors.aliyun.com/debian/ stretch-updates main non-free contrib" >>/etc/apt/sources.list && \
    echo "deb-src http://mirrors.aliyun.com/debian/ stretch-updates main non-free contrib" >>/etc/apt/sources.list && \
    echo "deb http://mirrors.aliyun.com/debian/ stretch-backports main non-free contrib" >>/etc/apt/sources.list && \
    echo "deb-src http://mirrors.aliyun.com/debian/ stretch-backports main non-free contrib" >>/etc/apt/sources.list

# 时区设定
RUN apt-get update && apt-get install -y --no-install-recommends tzdata  && rm -rf /var/lib/apt/lists/*
ENV TZ Asia/Shanghai

COPY . /app
WORKDIR /app

RUN chmod +x start.sh; \
    git clone https://github.com/Mitchell-Yuan/flask_demo.git; \
    pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com --upgrade pip ; \
    pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com -r /app/requirements.txt ;

EXPOSE 22
EXPOSE 80
EXPOSE 5000 

RUN mkdir /var/log/gun/

ENTRYPOINT ["gunicorn"]
CMD ["-w", "3", "-b", "0.0.0.0:5000", "--log-level=debug", "/app/flask-rest/manage:app", "--error-logfile /var/log/gun/error.log", "--access-logfile /var/log/gun/access.log"]