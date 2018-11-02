FROM python:3.6.5

ADD ./requirementsa.txt /

RUN mkdir /home/app && pip install -r /requirements.txt && apt update && \
    apt install -y nano python3-dev libpq-dev curl && useradd flask -m

USER flask
WORKDIR /home/app

EXPOSE 5000

CMD ["python", "main.py"]
