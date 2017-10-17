/bin/bash -c  "source /virtualenv-icas/bin/activate"

service nginx start

uwsgi --ini /project/wsgi/uwsgi.ini
