FROM ubuntu:16.04

RUN echo "deb http://archive.ubuntu.com/ubuntu xenial main universe" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y build-essential git
RUN apt-get install -y python python-dev python-setuptools
RUN apt-get install -y nginx supervisor
RUN easy_install pip

# install uwsgi now because it takes a little while
RUN pip install uwsgi

# install nginx
RUN apt-get install -y software-properties-common python-software-properties
RUN apt-get update
RUN add-apt-repository -y ppa:nginx/stable
RUN apt-get install -y sqlite3

# install our code
add . /home/docker/code/

# setup all the configfiles
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN rm /etc/nginx/sites-enabled/default
RUN ln -s /home/docker/code/docker/nginx.conf /etc/nginx/sites-enabled/
RUN ln -s /home/docker/code/docker/supervisor.conf /etc/supervisor/conf.d/

# RUN pip install
RUN pip install -r /home/docker/code/requirements.txt

expose 80
cmd ["supervisord", "-n"]
