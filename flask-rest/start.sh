#! /usr/bin/env sh
gunicorn manage:app -b 0.0.0.0:5000 --workers 3
