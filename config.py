import os

BaseDir = os.path.abspath(os.path.dirname(__file__))
DbDir = os.path.join(BaseDir, 'db/')


class Config:
    SECURITY_KEY = os.environ.get('SECRET_KEY') or "'I dont know what's that!"

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    MONGODB_SETTINGS = {
        'db': 'local',
        'host': 'localhost',
        'port': 27017
    }


class ProductionConfig(Config):
    pass


class TestingConfig(Config):
    pass


config = {
    'develop': DevelopmentConfig,
    'test': TestingConfig,
    'product': ProductionConfig,
    'default': DevelopmentConfig
}
