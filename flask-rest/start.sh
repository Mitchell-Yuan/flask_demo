#! /usr/bin/env sh
set -e
/bin/bash /etc/profile

rm /etc/nginx/nginx.conf
cd /flask-rest
cp nginx.conf /etc/nginx/

service nginx start
service nginx status

mkdir /var/log/gun/
/usr/local/bin/gunicorn manage:app -b 0.0.0.0:5000 -w 3 -t 300 --log-level=debug --graceful-timeout 300 --error-logfile /var/log/gun/error.log --access-logfile /var/log/gun/access.log
# /usr/local/bin/python3 /app/flask-rest/manage.py startserver