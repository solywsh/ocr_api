FROM ubuntu

RUN apt-get install --assume-yes apt-utils
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev && \
    apt-get install -y nginx uwsgi uwsgi-plugin-python3
RUN apt-get install -y language-pack-zh-hans

ENV LC_ALL="zh_CN.UTF-8"

COPY ./requirements.txt /requirements.txt
COPY ./nginx.conf /etc/nginx/nginx.conf
#COPY ./english_g2 ~/.EasyOCR/model
#COPY ./zh_sim_g2 ~/.EasyOCR/model

WORKDIR /

RUN pip3 install -r requirements.txt

COPY . /

RUN adduser --disabled-password --gecos '' nginx\
  && chown -R nginx:nginx /app \
  && chmod 777 /run/ -R \
  && chmod 777 /root/ -R

ENTRYPOINT [ "/bin/bash", "/entry-point.sh"]