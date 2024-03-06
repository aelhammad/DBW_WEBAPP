import random
import string

class DevelopmentConfig():
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql://dbwapp:toxicdb33@localhost/toxbrowser'
    SECRET_KEY = 'abcabcabcabcabcabc'

class ProductionConfig():
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql://dbwapp:toxicdb33@localhost/toxbrowser'
    SECRET_KEY = ''.join(random.choices(string.ascii_letters, k=30))

config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}

PREFIX = "/toxbrowser"
