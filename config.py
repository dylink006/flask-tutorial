class Config(object):
    DEBUG = False
    TESTING = False

    SECTRET_KEY = "efbnrhgrbejnenwkd"

    DB_NAME = "production-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "example"

    UPLOADS = "/home/username/app/app/static/images/uploads"

    SESSION_COOKIE_SECURE = True

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

    DB_NAME = "development-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "example"

    UPLOADS = "/home/username/projects/flask-test/app/app/static/images/uploads"

    SESSION_COOKIE_SECURE = False
    

class TestingConfig(Config):
    TESTING = True

    DB_NAME = "testing-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "example"

    UPLOADS = "/home/username/projects/flask-test/app/app/static/images/uploads"

    SESSION_COOKIE_SECURE = False
