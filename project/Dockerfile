FROM python:2.7
WORKDIR /app
COPY ./techtrends .

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install \
    python3-pip

RUN pip3 install -r requirements.txt
RUN python3 init_db.py

EXPOSE 7111

CMD [ "python3", "app.py" ]
