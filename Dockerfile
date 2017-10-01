FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /asm
WORKDIR /asm
ADD requirements.txt /asm/
RUN pip install -r requirements.txt
ADD . /asm/

