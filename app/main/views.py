# coding:utf-8
from flask import redirect, request, jsonify
import time
import json
from .. import db
from ..db_models import Admin, Articles, Thoughts
from . import main
from app import *


@main.route("/")
def index():
    return redirect("/static/index.html")


@main.route("/post", methods=['POST'])
def post():
    """to post article for admin"""
    data = request.form
    if (data):
        pwd = data.get("pwd")
        check = Admin.query.filter_by(pwd=pwd).first()
        if (check):
            title = data.get("title")
            summary1 = data.get("summary1")
            summary2 = data.get("summary2")
            content = data.get("content")
            art_type = data.get("art_type")
            pic_key = data.get("key")
            if (title and summary1 and summary2 and content and art_type and pic_key):
                new_art = Articles(title=title, summary1=summary1,
                                   summary2=summary2, content=content,
                                   art_type=art_type, pic_key=pic_key)
                db.session.add(new_art)
                db.session.commit()
                return "done"
            else:
                return "invalid"
        else:
            return "deny"
    else:
        return "nodata"


@main.route("/modify", methods=['POST'])
def modify():
    """modify article by admin"""
    data = request.form
    if data:
        pwd = data.get("pwd")
        check = Admin.query.filter_by(pwd=pwd).first()
        if check:
            try:
                id_ = int(data.get("id"))
                title = data.get("title")
                summary1 = data.get("summary1")
                summary2 = data.get("summary2")
                content = data.get("content")
                art_type = data.get("art_type")
                pic_key = data.get("key")
                if (id_ and title and summary1 and summary2 and content and art_type and pic_key):
                    art = Articles.query.filter_by(id=id_).first()
                    if (art):
                        art.title = title
                        art.summary1 = summary1
                        art.summary2 = summary2
                        art.content = content
                        art.art_type = art_type
                        art.pic_key = pic_key
                        db.session.commit()
                        return "done"
                    else:
                        return "inexsit"
                else:
                    return "invalid"
            except:
                return "something wrong"
        else:
            return "deny"
    else:
        return "nodata"


@main.route("/postthoughts", methods=["POST"])
def postThoughts():
    content = request.form.get("thoughts")
    pwd = request.form.get("pwd")
    check = Admin.query.filter_by(pwd=pwd).first()
    if check:
        if (content):
            new_thoughts = Thoughts(content=content)
            db.session.add(new_thoughts)
            db.session.commit()
            return "done"
        else:
            return "no content"
    else:
        return "deny"


@main.route('/test', methods=['POST'])
def test():
    account = request.form.get('username')
    pwd = request.form.get('pwd')
    print "Account:", account
    print "password:", pwd
    return redirect('http://qzone.qq.com/')
