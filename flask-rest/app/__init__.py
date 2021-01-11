#!/usr/bin/env python
# -*- coding:utf-8 -*-
import flask
from app.config import config


def create_app(config_name='default'):
    # templates文件夹位置, '.'代表当前目录位置, 所以'..'代表上级目录
    app = flask.Flask(__name__, template_folder='../templates', static_folder="../static")
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .main import main as main_blueprint # 引入蓝本实例
    app.register_blueprint(main_blueprint) # 注册蓝本到app

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    # 以/auth开头的接口被划分到蓝图anth中,整个应用层次更清晰

    return app