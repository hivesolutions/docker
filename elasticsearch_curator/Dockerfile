FROM hivesolutions/python

WORKDIR /curator

ENV CURATOR_UNIT days
ENV CURATOR_COUNT 15

RUN ln -s /curator /root/.curator
RUN pip3 install elasticsearch-curator==5.5

CMD ["/run.sh"]
