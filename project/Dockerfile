FROM python:2.7

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install \
    python3-pip

WORKDIR /techtrends

COPY requirements.txt /techtrends/requirements.txt
RUN pip3 install -r requirements.txt

COPY app.py /techtrends/app.py
COPY init_db.py /techtrends/init_db.py

RUN flask init-db

EXPOSE 3111

CMD [ "python3", "app.py" ]
