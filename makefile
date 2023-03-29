.DEFAULT_GOAL := build

build:
	docker build -t my-starwars-app .
.PHONY: build

run:
	docker run -p 3000:3000 my-starwars-app
.PHONY: run
