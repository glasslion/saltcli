FROM        jacksoncage/salt
MAINTAINER  Leo Zhou "glasslion<at>gmail.com"
ENV REFRESHED_AT 2015-10-01

RUN apt-get remove python-pip -y
RUN curl -o /tmp/get-pip.py https://bootstrap.pypa.io/get-pip.py && \
          python /tmp/get-pip.py
ADD requirements_docker.txt /tmp/saltapi/requirements_docker.txt
RUN pip install -r /tmp/saltapi/requirements_docker.txt

ADD docker_start.sh /start.sh
CMD ["bash", "/start.sh"]
