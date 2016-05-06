#coding:utf-8
from app import create_app, db
from app.db_models import Admin, Articles

app = create_app("dev")

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)
