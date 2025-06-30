from dataclasses import asdict

from celery import Celery
from dependency_injector.containers import (
    DeclarativeContainer,
    WiringConfiguration,
)
from dependency_injector.providers import Factory, Singleton

from consumer.actions.cpu_heavy_lifting import CPUHeavyLifting
from consumer.actions.io_heavy_lifting import IOHeavyLifting
from consumer.celeryconfig import CeleryConfig


class ConsumerContainer(DeclarativeContainer):
    wiring_config = WiringConfiguration(modules=["consumer.main"])

    celery: Singleton[Celery] = Singleton(
        Celery,
        main="consumer",
        **asdict(CeleryConfig()),
    )

    io_heavy_lifting_action: Factory[IOHeavyLifting] = Factory(
        IOHeavyLifting,
        celery=celery,
    )
    cpu_heavy_lifting_action: Factory[CPUHeavyLifting] = Factory(
        CPUHeavyLifting,
        celery=celery,
    )
