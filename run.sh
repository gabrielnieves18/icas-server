sudo docker run \
-it -p 80:80 -p 443:443 --rm \
-v $(pwd)/project:/project:rw \
icas-nginx-django:v0.12.0 \
