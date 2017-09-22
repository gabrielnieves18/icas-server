FROM python:3.6

# Set multiple labels at once, using line-continuation characters to break long lines
LABEL vendor=ICAS\ Incorporated \
      com.example.is-beta="true" \
      com.example.is-production="false" \
      com.example.version="0.0.1-beta" \
      com.example.release-date="2017-09-21"

ENV PYTHONUNBUFFERED 1

VOLUME ["/project"]

WORKDIR /project

COPY project/requirements.txt /project/

RUN pip install -r /project/requirements.txt

ADD . /project/

CMD [ "/bin/bash" ]
