FROM alpine:3.7
LABEL Sean Bradley  <seanwasere@gmail.com>

RUN apk update
RUN apk add nodejs 
RUN apk add nginx
RUN set -x ; \
  addgroup -g 82 -S www-data ; \
  adduser -u 82 -D -S -G www-data www-data && exit 0 ; exit 1

COPY ./nginx.conf	    /etc/nginx/nginx.conf
#COPY ./localhost.crt	/etc/nginx/localhost.crt
#COPY ./localhost.key	/etc/nginx/localhost.key
COPY ./AngularApp /AngularApp
WORKDIR /AngularApp
RUN npm install 
RUN npm install -g @angular/cli@7.3.5
RUN ng build --prod

COPY ./AngularApp/dist/AngularApp   /www
