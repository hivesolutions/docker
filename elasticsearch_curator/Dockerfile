FROM python:3.6-alpine

WORKDIR /curator

ENV CURATOR_HOST elasticsearch
ENV CURATOR_UNIT days
ENV CURATOR_COUNT 15

ADD run.sh /run.sh

RUN apk update && apk add bash
RUN ln -s /curator /root/.curator
RUN pip3 install "elasticsearch-curator<7"

CMD ["/run.sh"]
