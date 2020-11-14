import os
from dotenv import load_dotenv


load_dotenv()


class BaseConfig(object):

    SECRET_KEY = os.getenv('APP_SECRET_KEY', 'secret_key')
    JSON_AS_ASCII = False


class DevelopmentConfig(BaseConfig):

    DEBUG = True


class ProductionConfig(BaseConfig):

    DEBUG = False


class TestingConfig(BaseConfig):

    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False


config_by_name = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig,
    test=TestingConfig
)

