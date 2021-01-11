#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Config:
    CACHE_TYPE = 'simple' # Flask-Caching related configs
    CACHE_DEFAULT_TIMEOUT = 300
    SECRET_KEY = None
    JSONIFY_MIMETYPE = 'application/json'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    # TESTING = True

config = {
    'development':DevelopmentConfig,
    'default':DevelopmentConfig
}