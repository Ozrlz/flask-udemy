FROM python:3.6.5

ADD ./requirements.txt /

RUN mkdir /home/app && pip install -r /requirements.txt && apt update && \
    apt install -y nano python3-dev libpq-dev curl && useradd flask -m

USER flask
WORKDIR /home/app
ADD uwsgi.ini .

EXPOSE 5000 5001

CMD ["uwsgi", "--master", "--emperor", "uwsgi.ini", "--die-on-term", "--uid", "flask", "--gid", "flask"]
