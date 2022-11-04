# test-rtd

Calcula cuanto hay que pagarle a los jugadores en base a su desempeño por equipo.

Se cuenta con documentacion en `localhost:8000/docs` que se puede probar.

Parar correrlo se necesita tener [docker](https://www.docker.com/) y [make](https://www.gnu.org/software/make/)

1. `make build`
2. `make up` para ver el log `upd` detached
3. `make down` o `ctrl+c`

## Live version

https://backend-tciy4cvxsq-uw.a.run.app/docs

# Se puede correr mediante make

```
$ make help
███████╗██╗   ██╗███████╗██╗     ██████╗  ██████╗ ███████╗
██╔════╝██║   ██║██╔════╝██║     ██╔══██╗██╔═══██╗██╔════╝
███████╗██║   ██║█████╗  ██║     ██║  ██║██║   ██║███████╗
╚════██║██║   ██║██╔══╝  ██║     ██║  ██║██║   ██║╚════██║
███████║╚██████╔╝███████╗███████╗██████╔╝╚██████╔╝███████║
╚══════╝ ╚═════╝ ╚══════╝╚══════╝╚═════╝  ╚═════╝ ╚══════╝
help                 This Help
build                Build container
up                   Container up
upd                  Container detached up
down                 Shutdown container
sh                   Shell into running container
tests                Run tests on running container
tests-vvv            Run verbose tests on running container
black                Apply black to code
install-gcloud-linux Google install gcloud components on Linux
upgrade-gcloud       Google upgrade gcloud components
deploy-normal        Google deploy without all traffic usage `email=...@gmail.com project=project-name make deploy`
deploy-production    google promoting all traffic to new version usage `email=...@gmail.com project=project-name make deploy-production`
deploy               google deploy with default all
----------------------------------------------------------
```

# Docker

1. `docker-compose up -d --build`
2. `docker-compose up`
3. Abrir http://localhost:8000/docs

# curl

```curl
curl --location --request POST 'localhost:8000/api/sueldo/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "jugadores": [
        {
            "nombre": "Juan",
            "nivel": "A",
            "goles": 6,
            "sueldo": 50000,
            "bono": 15000,
            "sueldo_completo": null,
            "equipo": "rojo"
        },
        {
            "nombre": "Pedro",
            "nivel": "B",
            "goles": 9,
            "sueldo": 60000,
            "bono": 20000,
            "sueldo_completo": null,
            "equipo": "rojo"
        },
        {
            "nombre": "Martín",
            "nivel": "C",
            "goles": 10,
            "sueldo": 70000,
            "bono": 25000,
            "sueldo_completo": null,
            "equipo": "rojo"
        },
        {
            "nombre": "Luis",
            "nivel": "Cuauh",
            "goles": 30,
            "sueldo": 100000,
            "bono": 50000,
            "sueldo_completo": null,
            "equipo": "rojo"
        },
        {
            "nombre": "Carlos",
            "nivel": "Cuauh",
            "goles": 6,
            "sueldo": 100000,
            "bono": 15000,
            "sueldo_completo": null,
            "equipo": "azul"
        },
        {
            "nombre": "Peter",
            "nivel": "C",
            "goles": 9,
            "sueldo": 70000,
            "bono": 20000,
            "sueldo_completo": null,
            "equipo": "azul"
        },
        {
            "nombre": "Francisco",
            "nivel": "B",
            "goles": 10,
            "sueldo": 60000,
            "bono": 25000,
            "sueldo_completo": null,
            "equipo": "azul"
        },
        {
            "nombre": "Jair",
            "nivel": "A",
            "goles": 30,
            "sueldo": 50000,
            "bono": 50000,
            "sueldo_completo": null,
            "equipo": "azul"
        }
    ]
}'
```