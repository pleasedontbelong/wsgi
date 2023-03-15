FROM tiangolo/uwsgi-nginx:python3.11
COPY nginx.conf /etc/nginx/nginx.conf

RUN apt update
RUN apt install htop

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
COPY . /app

EXPOSE 8000

CMD gunicorn --workers=2 --log-level debug --bind=0.0.0.0:8000 --statsd-host=${STATSD_HOST}:${STATSD_PORT} --statsd-prefix=${APP_NAME} app:application 
