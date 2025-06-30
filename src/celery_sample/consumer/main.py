import logging

from dependency_injector.wiring import Provide, inject

from consumer.actions.cpu_heavy_lifting import (
    CPUHeavyLifting,
    CPUHeavyLiftingRequest,
)
from consumer.actions.io_heavy_lifting import (
    IOHeavyLifting,
    IOHeavyLiftingRequest,
)
from consumer.bootstrap.container import ConsumerContainer
from consumer.bootstrap.heavy_lifting_request import HeavyLiftingTask

logger = logging.getLogger(__name__)

consumer_container = ConsumerContainer()
consumer_container.wire(modules=[__name__])
celery = consumer_container.celery()


@celery.task(
    base=HeavyLiftingTask,
    name="test.io_bound",
    acks_late=True,
    task_acks_on_failure_or_timeout=True,
    autoretry_for=(ValueError,),
    retry_kwargs={"max_retries": 3, "countdown": 2},
    worker_concurrency=12,
    worker_deduplicate_successful_tasks=False,
)
@inject
def run_io_heavy_lifting(
    data: str,
    io_heavy_lifting: IOHeavyLifting = Provide[
        ConsumerContainer.io_heavy_lifting_action
    ],
) -> None:
    input_ = IOHeavyLiftingRequest(message=data)
    io_heavy_lifting(data=input_)


@celery.task(
    base=HeavyLiftingTask,
    name="test.cpu_bound",
    acks_late=True,
    task_acks_on_failure_or_timeout=True,
    autoretry_for=(ValueError,),
    retry_kwargs={"max_retries": 3, "countdown": 2},
    worker_concurrency=12,
    worker_deduplicate_successful_tasks=False,
)
@inject
def run_cpu_heavy_lifting(
    data: str,
    cpu_heavy_lifting: CPUHeavyLifting = Provide[
        ConsumerContainer.cpu_heavy_lifting_action
    ],
) -> None:
    input_ = CPUHeavyLiftingRequest(message=data)
    cpu_heavy_lifting(data=input_)
