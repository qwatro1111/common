import os

class Config:
    SECRET_KEY = 'my_secret_key'

class TestConfig:
    SECRET_KEY = 'my_test_secret_key'

class ProdConfig:
    SECRET_KEY = 'my_prod_secret_key'

def run_config():
    env = os.environ.get("ENV")
    if env == "TEST":
        return TestConfig
    elif env == "PROD":
        return ProdConfig
    return Config
