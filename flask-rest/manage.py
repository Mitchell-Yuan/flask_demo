#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, request, render_template, jsonify, Blueprint
from flask import abort, Response, render_template_string, send_from_directory
from flask_script import Manager, Shell, Server
from flasgger import Swagger, swag_from
from flask_compress import Compress
from app import create_app
import datetime
import time
import json
import os
# from flask_caching import Cache
from flask_bootstrap import Bootstrap

app = create_app(config_name='default')

swagger_config = Swagger.DEFAULT_CONFIG
swagger_config['title'] = 'Flask'
swagger_config['swagger_ui_standalone_preset_js'] = '//unpkg.com/swagger-ui-dist@3/swagger-ui-standalone-preset.js'
swagger_config['jquery_js'] = '//unpkg.com/jquery@2.2.4/dist/jquery.min.js'
swagger_config['swagger_ui_css'] = '//unpkg.com/swagger-ui-dist@3/swagger-ui.css'
swagger_config['specs_route'] = '/api'

# Swagger(app, config=swagger_config)
Compress(app)
bootstrap = Bootstrap(app)
manager = Manager(app)

# access python shell with context
manager.add_command(
	"shell",
	Shell(make_context=lambda: {'app': app}), use_ipython=True)

# run the app
manager.add_command(
	"startserver",
	Server(port=(os.getenv('FLASK_PORT') or 5000), host='0.0.0.0'))


if __name__ == '__main__':
    '''
    from livereload import Server

    live_server = Server(app.wsgi_app)
    live_server.watch('**/*.*')
    live_server.serve(open_url_delay=True)
    '''
    # flask 多线程: threaded=True, 多进程(linux&mac支持): processes=4, 多线程与多进程不能同时使用。
    app.run('127.0.0.1', '5000')
    # manager.run() # python manage.py startserver