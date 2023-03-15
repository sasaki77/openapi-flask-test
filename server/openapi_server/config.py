class Config(object):
    Testing = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    Testing = True


config = {
    "development": "openapi_server.config.DevelopmentConfig",
    "testing": "openapi_server.config.TestingConfig",
    "default": "openapi_server.config.DevelopmentConfig",
}
