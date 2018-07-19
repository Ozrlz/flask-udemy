FROM python:3.6.5

ADD ./requirements.txt /

RUN mkdir /home/app && pip install -r /requirements.txt

WORKDIR /home/app

EXPOSE 5000

CMD ["python", "main.py"]

