from dataclasses import asdict

from celery import Celery
from dependency_injector import containers
from dependency_injector.providers import Factory, Singleton

from producer.actions.send_message import SendMessage
from producer.celeryconfig import CeleryConfig


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["producer.router"])

    celery: Singleton[Celery] = Singleton(
        Celery, main="producer", **asdict(CeleryConfig()),
    )

    send_message: Factory[SendMessage] = Factory(SendMessage, celery=celery)
