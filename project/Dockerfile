FROM nginx:1.13.5

# Set multiple labels at once, using line-continuation characters to break long lines
LABEL vendor=ICAS\ Incorporated \
      com.example.is-beta="true" \
      com.example.is-production="false" \
      com.example.version="v0.0.1-beta" \
      com.example.release-date="2017-10-11"

ENV MEDIA_ROOT /icas/media
ENV STATIC_ROOT /icas/static
ENV UWSGI_PARAMS /uwsgi_params


VOLUME ["/icas/media", "/icas/static"]

COPY /icas_nginx.conf /etc/nginx/sites-enabled/
# COPY $MEDIA_ROOT /icas/media
# COPY $STATIC_ROOT /icas/static
COPY $UWSGI_PARAMS /

EXPOSE 80

# CMD [ "/bin/bash" ]

CMD ["nginx", "-g", "daemon off;"]
