FROM ubuntu:18.04
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

COPY src /source
COPY tests /tests
COPY setup.cfg /

WORKDIR /source

COPY requirements.txt /source/requirements.txt
RUN pip install -r requirements.txt

CMD python run.py