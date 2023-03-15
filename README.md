## build docker image
docker build -t custom-nginx .

## run container
docker run -it --rm --name nginx-container custom-nginx bash

## start gunicorn
gunicorn --workers=2 --max_requests=2 --log-level debug --bind=0.0.0.0:8000 --statsd-host=$STATSD_HOST:$STATSD_PORT --statsd-prefix=$APP_NAME app:application 