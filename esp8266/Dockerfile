FROM alpine:latest

LABEL version="1.0"
LABEL maintainer="Hive Solutions <development@hive.pt>"

RUN apk update && apk add --no-cache bash

ADD build.sh /build.sh
ADD build.root.sh /build.root.sh

RUN /build.root.sh

RUN adduser -D -S -s /bin/bash builder

USER builder

RUN /build.sh

CMD ["/bin/bash"]
