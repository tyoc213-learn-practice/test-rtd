help: ## This Help
	@echo '███████╗██╗   ██╗███████╗██╗     ██████╗  ██████╗ ███████╗'
	@echo '██╔════╝██║   ██║██╔════╝██║     ██╔══██╗██╔═══██╗██╔════╝'
	@echo '███████╗██║   ██║█████╗  ██║     ██║  ██║██║   ██║███████╗'
	@echo '╚════██║██║   ██║██╔══╝  ██║     ██║  ██║██║   ██║╚════██║'
	@echo '███████║╚██████╔╝███████╗███████╗██████╔╝╚██████╔╝███████║'
	@echo '╚══════╝ ╚═════╝ ╚══════╝╚══════╝╚═════╝  ╚═════╝ ╚══════╝'
	@perl -nle'print $& if m{^[a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
	@echo '----------------------------------------------------------'

.PHONY: tests

sh: ## shell into container
	docker-compose exec fastapi /bin/bash

tests: ## run tests on current
	docker-compose exec fastapi pytest tests

build: ## build
	docker-compose up -d --build

upd: ## detached up
	docker-compose up -d

up: ## up
	docker-compose up

down: ## down
	docker-compose down

black:
	docker-compose exec fastapi pip install black
	docker-compose exec fastapi black -t py310 .

