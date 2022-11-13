FROM python:3.8
USER root
RUN apt-get update
RUN apt-get install -y cron systemctl rsyslog vim
RUN apt-get install -y gcc
RUN apt-get install -y default-libmysqlclient-dev
RUN apt-get install -y postgresql
RUN apt-get install python3-psycopg2
RUN apt-get install -y python3-dev
RUN apt-get install -y python3-setuptools build-essential
RUN apt-get install libpq-dev
# Install cron.
RUN apt-get install -y cron systemctl rsyslog nano
# Create the log file to be able to run tail
#RUN touch /var/log/cron.log
# Run the command on container startup
#CMD systemctl enable cron && systemctl start cron

ENV PYTHONUNBUFFERED=1
WORKDIR /vps_effort_server
COPY requirements.txt /test_alex_server/
RUN pip install ez_setup
RUN pip install uwsgi
RUN pip install celery
RUN pip install redis
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . /test_alex_server/
