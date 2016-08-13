# coding:utf-8
from . import db
from sqlalchemy.sql import func


class Admin(db.Model):
    """table for admin"""
    __tablename__ = "admin"
    pwd = db.Column(db.String(64), primary_key=True)


class Articles(db.Model):
    """table for articles of admin"""
    __tablename__ = "articles"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    summary1 = db.Column(db.Text)
    summary2 = db.Column(db.Text)
    content = db.Column(db.Text)
    art_type = db.Column(db.String(16))  # type of article
    pic_key = db.Column(db.String(128), server_default="cover")  # key of cover picture on qiniu
    time = db.Column(db.TIMESTAMP, server_default=func.now())


class Thoughts(db.Model):
    """docstring for thoughts"""
    __tablename__ = "thoughts"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(512))
    time = db.Column(db.TIMESTAMP, server_default=func.now())
