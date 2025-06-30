from fastapi import FastAPI

from producer.router import producer_router


def fastapi_bootstrap() -> FastAPI:
    app = FastAPI()
    app.include_router(router=producer_router)
    return app
