from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.sueldo import router as api_router

description = """
Sueldos API te deja calcular el `pago_total` de cada jugador en la liga de ⚽.

## Sueldos

Puedes mandar una petición `post` a `https://backend-tciy4cvxsq-uw.a.run.app/api/sueldo/` ver el ejemplo correpondiente.

* Se puede omitir la lista de `niveles`.
* Si un jugador tiene un nivel que no esta en la lista de niveles, se toma un valor de 100 como minimo.
* Se calcula el salario por equipo independientemente de cuantos equipos se manden.

### src

[https://github.com/tyoc213-learn-practice/test-rtd](https://github.com/tyoc213-learn-practice/test-rtd)

### live version

[https://backend-tciy4cvxsq-uw.a.run.app/docs](https://backend-tciy4cvxsq-uw.a.run.app/docs)

###NOTE
 
Tambien contiene los endpoints iniciales que se dejaron para el histórico.
"""


def get_application():
    app = FastAPI(title="test_rtd", version="0.0.1", description=description)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router, prefix="/api")

    return app


app = get_application()


@app.get("/")
async def root():
    return {"message": "Hello World"}
