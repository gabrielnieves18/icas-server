# README #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###

* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

## Configuration ##

To-Do

## Dependencies ##

 * [Docker](https://docs.docker.com/engine/installation/)

## Deployment instructions ##

### Build django image  ###

<code>
sudo docker build . -t django:1.11.0
</code>

<code>
To satrt the server run the following code:
	docker run -it --rm -v $(pwd)/project:/project django:1.11.0 python manage.py runserver
</code>

### Who do I talk to? ###

* Gabriel Nieves Ponce: nieves1@umbc.edu
