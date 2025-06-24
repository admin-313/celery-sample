from celery import Celery
from dependency_injector import containers
from dependency_injector.providers import Factory, Singleton

from producer.actions.send_message import SendMessage


class Container(containers.DeclarativeContainer):
    celery: Singleton[Celery] = Singleton(
        Celery,
        main="worker",
        broker="pyamqp://guest:guest@172.20.0.2:5672//",
        backend="redis://:RvPtXZyLRxRd7zvj3mieYvXAQAQH9Cjw@172.20.0.2:6379/0",
    )

    send_message: Factory[SendMessage] = Factory(SendMessage, celery=celery)
