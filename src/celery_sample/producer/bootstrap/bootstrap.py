from fastapi import FastAPI

from producer.bootstrap.containers import Container
from producer.router import producer_router


def fastapi_bootstrap() -> FastAPI:
    container = Container()
    app = FastAPI()
    app.include_router(router=producer_router)
    return app
