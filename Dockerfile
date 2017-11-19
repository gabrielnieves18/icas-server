FROM ubuntu:16.04

# Set multiple labels at once, using line-continuation characters to break long lines
LABEL vendor=ICAS\ Incorporated \
      com.example.is-beta="true" \
      com.example.is-production="false" \
      com.example.version="0.0.1-beta" \
      com.example.release-date="2017-09-21"

ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONUNBUFFERED 1
ENV PROJECT_ROOT /project
ENV ICAS_NGINX_CONFIG $PROJECT_ROOT/nginx/icas_nginx.conf
ENV REQUIREMENTS $PROJECT_ROOT/requirements.txt
ENV WSGI_ROOT $PROJECT_ROOT/wsgi
ENV UWSGI_INI_SCRIPT $WSGI_ROOT/uwsgi.ini
ENV VIRTUALENV_ROOT /virtualenv-icas

VOLUME [ \
	"/project", \
	"/virtualenv-icas", \
]

WORKDIR /project

COPY $REQUIREMENTS $PROJECT_ROOT
COPY $PROJECT_ROOT/start_server.sh $PROJECT_ROOT
COPY $UWSGI_INI_SCRIPT $WSGI_ROOT

# Upgrdae repo list and binaries
RUN apt-get update
RUN apt-get install -y --no-install-recommends apt-utils
RUN apt-get upgrade -y

# Install python3.5 and pip3
RUN apt-get install -y python3.5 \
			python3-pip 

RUN pip3 install --upgrade pip && \
    pip3 install virtualenv

# Create virtualenv and activate it
RUN virtualenv $VIRTUALENV_ROOT
RUN /bin/bash -c "source $VIRTUALENV_ROOT/bin/activate"

# Install all python requirements
RUN pip install -r $REQUIREMENTS

# Install nginx
RUN apt-get install nginx -y

# Copy the icas nginx configuration
COPY $ICAS_NGINX_CONFIG /etc/nginx/sites-enabled/

# Install Dependencies for Certbo. An 
# Open source client hat fetches and 
# deploys SSL/TLS certificates in order
# to enable HTTPS connection to our site
RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:certbot/certbot && apt-get update
# Run this manually with answers 2 and 105: 
# RUN apt-get install -y python-certbot-nginx 

# Enable interactive before exiting
ENV DEBIAN_FRONTEND teletype

CMD [ "sh", "start_server.sh"]
