### What is this repository for? ###

To-Do

## Configuration ##

To-Do

## Dependencies ##

 * [Docker](https://docs.docker.com/engine/installation/)

## Deployment instructions ##

### Build django image  ###

```
sudo docker build . -t django:1.11.0
```

```
To start the server run the following code:
	docker run -it --rm -v $(pwd)/project:/project:rw -p 8000:8000  django:1.11.0 python icas/manage.py runserver 0:8000
```

### Who do I talk to? ###

* Gabriel Nieves Ponce: gabrielnieves18@gmail.com
