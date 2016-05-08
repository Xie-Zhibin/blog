# coding:utf-8
from flask import redirect, request, jsonify
import time
import json
from .. import db
from ..db_models import Admin, Articles
from . import main
import markdown


@main.route("/")
def index():
    return redirect("/static/index.html")


@main.route("/postarticle", methods=['POST'])
def postarticle():
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
            artType = data.get("artType")
            picKey = data.get("key")
            if (title and summary1 and summary2 and content and artType and picKey):
                newArt = Articles(title=title, summary1=summary1,
                                  summary2=summary2,content=content,
                                  artType=artType, picKey=picKey)
                db.session.add(newArt)
                db.session.commit()
                return "done"
            else:
                return "invalid"
        else:
            return "deny"
    else:
        return "nodata"


@main.route("/api/index")
def apiIndex():
    """return two new articles"""
    arts = Articles.query.order_by(Articles.time.desc()).limit(2).all()
    raw_data = {"data": [], "status": 1}
    for i in arts:
        title = i.title
        time = i.time.strftime('%Y/%m/%d')
        id_ = i.id
        summary1 = i.summary1
        summary2 = i.summary2
        _type = i.artType
        key = i.picKey
        raw_data["data"].append({"title": title, "time": time, "id": id_,
                                 "summary1": summary1, "summary2": summary2, "type": _type, "key": key})
    json_data = json.dumps(raw_data)
    return json_data


@main.route("/api/getarts")
def apiGetArts():
    """return id,title,time,type etc. of each article"""
    type_ = request.args.get("type")
    count = request.args.get("count")
    raw_data = {"data": [], "status": 1}
    if (count):
        arts = Articles.query.order_by(Articles.time.desc()).limit(5).all()
    else:
        if (type_):
            arts = Articles.query.order_by(Articles.time.desc()).filter_by(
                artType=type_).all()
        else:
            arts = Articles.query.order_by(Articles.time.desc()).all()
    for i in arts:
        title = i.title
        time = i.time.strftime('%Y/%m/%d')
        id_ = i.id
        artType = i.artType
        raw_data["data"].append(
            {"title": title, "time": time, "id": id_, "type": artType})
    json_data = json.dumps(raw_data)
    return json_data


@main.route("/api/allarts")
def allArts():
    arts = Articles.query.order_by(Articles.time.desc()).all()
    raw_data = {"data": [], "status": 1}
    for i in arts:
        time = i.time.strftime('%Y/%m/%d')
        raw_data["data"].append({"id": i.id, "title": i.title,
                                 "summary": i.summary1, "type": i.artType, "time": time})
    json_data = json.dumps(raw_data)
    return json_data


@main.route("/api/sum")
def sum():
    all_num = Articles.query.count()
    coding_num = Articles.query.filter_by(artType="coding").count()
    others_num = all_num - coding_num
    raw_data = {"data": {"all": all_num, "coding": coding_num,
                         "others": others_num}, "status": 1}
    json_data = json.dumps(raw_data)
    return json_data


@main.route("/api/newestarts")
def apiNewestArts():
    """return the id of newest articel of coding and others"""
    others = Articles.query.order_by(Articles.time.desc()).filter_by(
        artType="others").first()

    coding = Articles.query.order_by(Articles.time.desc()).filter_by(
        artType="coding").first()
    data = {"data": {"coding": coding.id, "others": others.id}, "status": 1}
    json_data = json.dumps(data)
    return json_data


@main.route("/api/time")
def apiTime():
    """return the hours of this request"""
    hours = int(time.strftime("%H"))
    data = {"hours": hours, "status": 1}
    json_data = json.dumps(data)
    return json_data


@main.route("/api/art/<type>/<int:id>")
def apiArt(type, id):
    """get markdown from database to transform from md to html"""
    art = Articles.query.filter_by(id=id,artType=type).first()
    if (art):
        md = art.content
        response = markdown.markdown(md)
    else:
        response = "nothing"

    return response
