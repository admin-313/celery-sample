import logging

from dependency_injector.wiring import Provide, inject

from consumer.actions.heavy_lifting import (
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
    bind=True,
    base=HeavyLiftingTask,
    name="test.io_bound",
    acks_late=True,
    task_acks_on_failure_or_timeout=True,
    autoretry_for=(ValueError,),
    retry_kwargs={"max_retries": 3, "countdown": 2},
)
@inject
def run_heavy_lifting(
    self,
    data: str,
    heavy_lifting: IOHeavyLifting = Provide[
        ConsumerContainer.io_heavy_lifting_action
    ],
) -> None:
    input_ = IOHeavyLiftingRequest(message=data)
    heavy_lifting(data=input_)
