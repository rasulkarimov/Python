FROM alpine:latest

LABEL MAINTAINER="rasulkarimov"

RUN apk --update add nginx && \
    ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log && \
    mkdir /etc/nginx/sites-enabled/ && \
    mkdir -p /run/nginx && \
    rm -rf /etc/nginx/conf.d/default.conf && \
    rm -rf /var/cache/apk/*

COPY conf.d/app.conf /etc/nginx/conf.d/app.conf

RUN chgrp -R 0 /var/lib/nginx /run/nginx /etc/nginx && \
    chmod -R g=u /var/lib/nginx /run/nginx /etc/nginx

EXPOSE 8081
CMD ["nginx", "-g", "daemon off;"]
