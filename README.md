# What is this repository for?

This is a fully functional https enabled, nginx Django server. This is a project that I build for my course at UMBC.

Anyone can use it, but I would recommend updating the SSH certs provided by the nice folks [Let's Encrypt](https://letsencrypt.org/). 

To see the example website, visit this [page](https://creativecaco.com).

# Configuration 
## Dependencies

 * [Docker](https://docs.docker.com/engine/installation/)

## Deployment instructions

### Build django image 

```shell
sudo docker build . -t icas-nginx-django:v0.12.0
```
To start the server run the following code:
```shell
sudo docker run \
-it -p 80:80 -p 443:443 --rm \
-v $(pwd)/project:/project:rw \
icas-nginx-django:v0.12.0 \
```

## Disclaimer

This is not a production ready server by any means. It is meant to be used for learning purposes. Use at your risk!

# Who do I talk to?

* Gabriel Nieves Ponce: gabrielnieves18@gmail.com
