FROM python:3.8-buster

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /code

COPY src/* /code/

CMD ["kopf", "run", "handler.py", "-q"]
