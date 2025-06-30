from fastapi import FastAPI

from producer.bootstrap.bootstrap import fastapi_bootstrap
from producer.bootstrap.containers import Container


def main() -> FastAPI:
    container = Container()
    fastapi: FastAPI = fastapi_bootstrap()
    fastapi.container = container  # type: ignore[attr-defined]
    return fastapi


app = main()
