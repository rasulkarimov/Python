FROM python:3.6.8-alpine3.9

LABEL MAINTAINER="rasulkarimov"

ENV GROUP_ID=1000 \
    USER_ID=1000

WORKDIR /var/www/

RUN chgrp -R 0 /var/www/ && \
    chmod -R g=u /var/www/

ADD ./requirements.txt /var/www/requirements.txt
RUN pip install -r requirements.txt
ADD . /var/www/
RUN pip install gunicorn

RUN addgroup -g $GROUP_ID www
RUN adduser -D -u $USER_ID -G www www -s /bin/sh

USER www

EXPOSE 5000

CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", "wsgi"]
