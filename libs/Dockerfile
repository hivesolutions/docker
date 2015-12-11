FROM ubuntu:latest
MAINTAINER Hive Solutions

EXPOSE 8080

ENV LEVEL INFO
ENV SERVER netius
ENV SERVER_ENCODING gzip
ENV HOST 0.0.0.0
ENV PORT 8080
ENV CACHE 86400
ENV CORS 1

RUN apt-get update && apt-get install -y -q python python-setuptools python-dev python-pip git
RUN git clone https://github.com/hivesolutions/uxf_bin.git /libs/uxf
RUN git clone https://github.com/hivesolutions/layout.git /libs/layout
RUN git clone https://github.com/hivesolutions/pushi_js.git /libs/pushi
RUN git clone https://hive_development:4mBSDQdQzTW4NvmJ@bitbucket.org/hivesolutions/oibiquini.git && mv oibiquini/src/oibiquini/static /libs/oibiquini && rm -rf oibiquini
RUN pip install --upgrade netius

CMD BASE_PATH=/libs python -m netius.extra.filea
