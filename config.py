# coding:utf-8
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app():
        pass


class DevConfig(Config):
    DEBUG = True
    # 'mysql://root:xxxxxx@localhost/blog'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.db')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:xxxxxx@localhost/blog'


config = {
    "dev": DevConfig,
    "production": ProductionConfig
}
