from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.sueldo import router as api_router


def get_application():
    app = FastAPI(title="test_rtd", version="0.0.1")

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
