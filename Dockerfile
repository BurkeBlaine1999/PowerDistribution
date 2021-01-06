FROM python:3.8

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=app.py

CMD flask --host=0.0.0.0