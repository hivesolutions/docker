FROM hivesolutions/ubuntu:latest
MAINTAINER Hive Solutions

RUN echo "deb [arch=amd64] https://apt-mo.trafficmanager.net/repos/dotnet-release/ xenial main" > /etc/apt/sources.list.d/dotnetdev.list &&\
	apt-key adv --keyserver apt-mo.trafficmanager.net --recv-keys 417A0893 &&\
	apt-get update &&\
    apt-get install -y sudo gcc make pypy dotnet-dev-1.0.0 linux-headers-generic python-dev python3-dev pypy-dev

CMD ["/bin/bash"]
