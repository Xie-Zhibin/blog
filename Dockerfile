FROM ubuntu:14.04
MAINTAINER island <1159401236@qq.com>

RUN apt-get update
RUN apt-get install -y python3-dev
RUN apt-get install -y python3-pip
RUN apt-get clean
RUN apt-get autoclean

RUN pip3 install uwsgi

COPY requirements.txt /tmp/

RUN pip3 install -r /tmp/requirements.txt
RUN rm -f /tmp/requirements.txt

ADD . /blog
WORKDIR /blog

CMD ["uwsgi", "--ini", "blog_uwsgi.ini"]
