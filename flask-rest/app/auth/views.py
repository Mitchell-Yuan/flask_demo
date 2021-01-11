#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import abort, Response, render_template_string, send_from_directory
from flask import Flask, request, render_template, jsonify, Blueprint
import datetime
import time
import json
import os
import logging
import configparser
# 注册的蓝本
from . import auth

@auth.route('/', methods=['GET'])
def auth_page():
    try:
        return Response(render_template_string("""
        <html>
        <header>
            <h1 style="color:gold" align=center>Hello World</h1>
        </header>
        <body>
            <h2 style="color:plum" align=center>{{bar}}</h2>
        </body></html>
        """, bar=datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')), mimetype='text/html')
    except:
        abort(404) # 指定错误类型