FROM ubuntu:14.04

RUN apt-get update -y && apt-get install --no-install-recommends -y -q \
        build-essential \
        libpq-dev \
        python \
        python-dev \
        python-pip \
        libjpeg-dev \
    && apt-get clean \
    && apt-get autoclean \
    && apt-get autoremove -y \
    && rm -rf /var/lib/{apt,dpkg,cache,log}/

WORKDIR /app/

ADD ./src /app/

RUN pip install -e .[develop]

CMD ["python"]
