FROM hivesolutions/python:latest

LABEL version="1.0"
LABEL maintainer="Hive Solutions <development@hive.pt>"

EXPOSE 8080

ENV LEVEL INFO
ENV ENCODING gzip
ENV HOST 0.0.0.0
ENV PORT 8080
ENV CACHE 86400
ENV CORS 1
ENV BASE_PATH /libs

RUN git clone --depth=1 https://github.com/hivesolutions/uxf_bin.git /libs/uxf && rm -rf /libs/uxf/.git /libs/uxf/.settings /libs/uxf/.project /libs/uxf/README.md
RUN git clone --depth=1 https://github.com/hivesolutions/layout.git /libs/layout && rm -rf /libs/layout/.git /libs/layout/.settings /libs/layout/.project /libs/layout/README.md
RUN git clone --depth=1 https://github.com/hivesolutions/pushi_js.git /libs/pushi && rm -rf /libs/pushi/.git /libs/pushi/.settings /libs/pushi/.project /libs/pushi/README.md
RUN git clone --depth=1 https://x-token-auth:3YWfHHW8ZlpB2GdFgKJT@bitbucket.org/hivesolutions/oibiquini.git && mv oibiquini/src/oibiquini/static /libs/oibiquini && rm -rf oibiquini
RUN pip3 install --upgrade netius

CMD ["/usr/bin/python3", "-m", "netius.extra.filea"]
