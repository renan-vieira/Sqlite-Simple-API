FROM python:3.6.4

RUN mkdir /app
WORKDIR /app

COPY . /app

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y sqlite3

RUN pip3 install -r requirements.txt

EXPOSE 8080

#CMD ["python", "main.py"]