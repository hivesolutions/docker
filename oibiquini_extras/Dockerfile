FROM ubuntu:latest
MAINTAINER Hive Solutions

EXPOSE 8080

ENV LEVEL INFO
ENV SERVER netius
ENV SERVER_ENCODING gzip
ENV HOST 0.0.0.0
ENV PORT 8080
ENV MONGOHQ_URL mongodb://localhost:27017
ENV SHOPIFY_API_KEY SHOPIFY_API_KEY
ENV SHOPIFY_PASSWORD SHOPIFY_PASSWORD
ENV SHOPIFY_SECRET SHOPIFY_SECRET
ENV SHOPIFY_STORE SHOPIFY_STORE
ENV PYTHONPATH /oibiquini_extras/src

RUN apt-get update && apt-get install -y -q python python-setuptools python-dev python-pip git
RUN git clone https://hive_development:4mBSDQdQzTW4NvmJ@bitbucket.org/hivesolutions/oibiquini_extras.git
RUN pip install -r /oibiquini_extras/requirements.txt && pip install --upgrade netius

CMD python /oibiquini_extras/src/oibiquini_extras/main.py
