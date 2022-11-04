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

build: ## Build container
	docker-compose up -d --build

up: ## Container up
	docker-compose up

upd: ## Container detached up
	docker-compose up -d

down: ## Shutdown container
	docker-compose down

sh: ## Shell into running container
	docker-compose exec fastapi /bin/bash

tests: ## Run tests on running current
	docker-compose exec fastapi pytest tests

black:  ## Apply black to code
	docker-compose exec fastapi pip install black
	docker-compose exec fastapi black -t py310 .

install-gcloud-linux: ## Google install gcloud components on Linux
	sudo apt-get update && sudo apt-get install google-cloud-sdk google-cloud-sdk-app-engine-python
	gcloud init

upgrade-gcloud: ## Google upgrade gcloud components
	gcloud components update

deploy-normal: ## Google deploy without all traffic usage `email=...@gmail.com project=project-name make deploy`
	cd backend
	gcloud config set account ${email}
	gcloud config set project ${project}
	gcloud config set app/promote_by_default false
	gcloud config list
	gcloud run deploy --port 8000

deploy-production: ## google promoting all traffic to new version usage `email=...@gmail.com project=project-name make deploy-production`
	cd backend
	gcloud config set account ${email}
	gcloud config set project ${project}
	gcloud config set app/promote_by_default true
	gcloud config list
	gcloud run deploy --port 8000

deploy: ## google deploy with default all
	gcloud run deploy --port 8000
