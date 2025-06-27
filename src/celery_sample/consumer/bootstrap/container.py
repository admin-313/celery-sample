from dataclasses import asdict

from celery import Celery
from dependency_injector.containers import Container, WiringConfiguration
from dependency_injector.providers import Factory, Singleton

from consumer.actions.heavy_lifting import HeavyLifting
from consumer.celeryconfig import CeleryConfig


class ConsumerContainer(Container):
    wiring_config = WiringConfiguration(modules=["consumer.consumer"])

    celery: Singleton[Celery] = Singleton(
        Celery,
        main="consumer",
        **asdict(CeleryConfig()),
    )

    heavy_lifting_action: Factory[HeavyLifting] = Factory(
        HeavyLifting, celery=celery,
    )
