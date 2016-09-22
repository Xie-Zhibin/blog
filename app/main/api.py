"""Apis."""
from flask import request
import time
import json
from app.db_models import Articles, Thoughts
from app.main import main


@main.route("/api/index")
def api_index():
    """Return two new articles."""
    arts = Articles.query.order_by(Articles.time.desc()).limit(3).all()
    raw_data = {
        "data": [],
        "status": 1
    }
    for i in arts:
        title = i.title
        time = i.time.strftime('%Y/%m/%d')
        id_ = i.id
        summary1 = i.summary1
        summary2 = i.summary2
        _type = i.art_type
        key = i.pic_key
        raw_data["data"].append({"title": title, "time": time, "id": id_,
                                 "summary1": summary1, "summary2": summary2,
                                 "type": _type, "key": key})
    json_data = json.dumps(raw_data)
    return json_data


@main.route("/api/getarts")
def api_get_arts():
    """Return id,title,time,type etc. of each article."""
    type_ = request.args.get("type")
    count = request.args.get("count")
    raw_data = {"data": [], "status": 1}
    sum_ = Articles.query.count()
    if (count):
        arts = Articles.query.order_by(Articles.time.desc()).limit(5).all()

    else:
        if (type_):
            arts = Articles.query.order_by(Articles.time.desc()).filter_by(
                art_type=type_).all()
            sum_ = Articles.query.filter_by(art_type=type_).count()
        else:
            arts = Articles.query.order_by(Articles.time.desc()).all()
    for i in arts:
        title = i.title
        time = i.time.strftime('%Y/%m/%d')
        id_ = i.id
        art_type = i.art_type
        raw_data["data"].append(
            {"title": title, "time": time, "id": id_, "type": art_type})

    raw_data["sum"] = sum_
    json_data = json.dumps(raw_data)
    return json_data


@main.route("/api/allarts")
def all_arts():
    """Get all arts."""
    arts = Articles.query.order_by(Articles.time.desc()).all()
    raw_data = {"data": [], "status": 1}
    for i in arts:
        time = i.time.strftime('%Y/%m/%d')
        raw_data["data"].append({"id": i.id, "title": i.title,
                                 "summary": i.summary1, "type": i.art_type,
                                 "time": time})
    json_data = json.dumps(raw_data)
    return json_data


@main.route("/api/newestarts")
def api_newest_arts():
    """Return the id of newest articel of coding and others."""
    others = Articles.query.order_by(Articles.time.desc()).filter_by(
        art_type="others").first()

    coding = Articles.query.order_by(Articles.time.desc()).filter_by(
        art_type="coding").first()
    data = {
        "data": {
            "coding": coding.id,
            "others": others.id
        },
        "status": 1
    }
    json_data = json.dumps(data)
    return json_data


@main.route("/api/time")
def api_time():
    """Return the hours of this request."""
    hours = int(time.strftime("%H")) + 8
    data = {
        "hours": hours,
        "status": 1
    }
    json_data = json.dumps(data)
    return json_data


@main.route("/api/art/<type>/<int:id>")
def api_art(type, id):
    """Get markdown from database to transform from md to html."""
    art = Articles.query.filter_by(id=id, art_type=type).first()
    if (art):
        md = art.content
        response = md  # markdown.markdown(md)
    else:
        response = "nothing"

    return response


@main.route("/api/getthoughts")
def get_thoughts():
    """Get thoughts from db."""
    thoughts = Thoughts.query.order_by(Thoughts.time.desc()).first()
    data = {
        "data": thoughts.content,
        "status": 1
    }
    json_data = json.dumps(data)
    return json_data
