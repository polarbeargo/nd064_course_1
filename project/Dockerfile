FROM python:2.7

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install \
    python3-pip

WORKDIR /techtrends

COPY /techtrends/requirements.txt /techtrends/requirements.txt
RUN pip3 install -r requirements.txt

COPY /techtrends/app.py /techtrends/app.py
COPY /techtrends/init_db.py /techtrends/init_db.py

RUN python3 /techtrends/init_db.py

EXPOSE 7111

CMD [ "python3", "app.py" ]
