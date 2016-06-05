FROM hivesolutions/alpine_dev:latest
MAINTAINER Hive Solutions

EXPOSE 8080

ENV LEVEL INFO
ENV ENCODING gzip
ENV HOST 0.0.0.0
ENV PORT 8080
ENV CACHE 86400
ENV CORS 1
ENV BASE_PATH /libs

RUN git clone --depth=1 https://github.com/hivesolutions/uxf_bin.git /libs/uxf && rm -rf /libs/uxf/.git /libs/uxf/.project /lib/uxf/.settings
RUN git clone --depth=1 https://github.com/hivesolutions/layout.git /libs/layout && rm -rf /libs/layout/.git /libs/layout/.project /lib/layout/.settings
RUN git clone --depth=1 https://github.com/hivesolutions/pushi_js.git /libs/pushi && rm -rf /libs/pushi/.git /libs/pushi/.project /lib/pushi/.settings
RUN git clone --depth=1 https://hive_development:4mBSDQdQzTW4NvmJ@bitbucket.org/hivesolutions/oibiquini.git && mv oibiquini/src/oibiquini/static /libs/oibiquini && rm -rf oibiquini
RUN pip3 install --upgrade netius

CMD ["/usr/bin/python3", "-m", "netius.extra.filea"]
