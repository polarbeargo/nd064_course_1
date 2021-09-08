FROM python:2.7
WORKDIR /app
COPY ./techtrends .

RUN apt-get clean \
    && apt-get -y update

RUN pip install -r requirements.txt
RUN python init_db.py

EXPOSE 7111

CMD [ "python", "app.py" ]
