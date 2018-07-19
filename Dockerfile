FROM python:3.6.5

RUN mkdir /home/app

WORKDIR /home/app

EXPOSE 5000

CMD ["python", "main.py"]

