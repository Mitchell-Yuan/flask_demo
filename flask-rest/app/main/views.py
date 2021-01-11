#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import abort, Response, render_template_string, send_from_directory, url_for
from flask import Flask, request, render_template, jsonify, Blueprint, redirect
import datetime
import time
import json
import os
import logging
import configparser
# 注册的蓝本
from . import main


@main.route('/', methods=['GET'])
def upload_page():
    try:
        return render_template('upload.html', bar='', _upload_=url_for('.excel_get', page=-1))
        # return redirect("https://www.baidu.com")
    except Exception as e:
        print(e)
        # abort函数可以立即终止视图函数的执行
        # 并返回给前端特定的信息
        # 1 传递状态码信息, 必须是标准的http状态码
        abort(503)
        # return render_template('/web/404.html')
        # 2 传递响应体信息
        # resp = Response("login failed")
        # abort(resp)  # 返回Response响应对象

@main.route('/favicon.ico', methods=['GET'])
def favicon_get():
    try:
        return send_from_directory(directory='../static/', filename='favicon.ico', as_attachment=True)
    except:
        abort(503) # 指定错误类型

@main.route('/upload', methods=['POST'])
def excel_get():
    try:
        f = request.files['file']
        FileName = f.filename
        f.save(FileName)
        print(f.filename)
        # 处理函数 result = func(f.filename)
        result = 'Download succeed!'
        return jsonify({'result':result})
    except Exception as e:
        print(e)
        abort(503)