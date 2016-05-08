#coding:utf-8
from app import create_app, db
from app.db_models import Admin, Articles
from flask.ext.script import Manager

app = create_app("dev")
manager = Manager(app)

if __name__ == '__main__':
	manager.run()
    #app.run(host="0.0.0.0",port=80)
