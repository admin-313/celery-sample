from celery import Celery
from dependency_injector import containers, providers


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["producer.router"])
    celery: providers.Singleton[Celery] = providers.Singleton(
        Celery,
        main="worker",
        broker="pyamqp://guest:guest@172.20.0.2:5672//",
        backend="redis://:RvPtXZyLRxRd7zvj3mieYvXAQAQH9Cjw@172.20.0.2:6379/0",
    )
