import os
import datetime


class BaseConfig(object):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SECRET_KEY = 'super-secret'
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:@db:5432/postgres'


class ProductionConfig(BaseConfig):
    JWT_EXPIRATION_DELTA = datetime.timedelta(days=365)


CONFIG = dict(
    DEVELOPMENT=DevelopmentConfig,
    PRODUCTION=ProductionConfig,
).get(os.environ.get('ENVIRONMENT'), DevelopmentConfig)
