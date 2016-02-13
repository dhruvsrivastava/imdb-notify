# default config
import os

class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = 'my_precious'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///posts.db'

class DevelopmentConfig(BaseConfig):
	DEBUG = True

class ProductionConfig(BaseConfig):
	DEBUG = False