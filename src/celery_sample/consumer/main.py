import logging

from dependency_injector.wiring import Provide, inject

from consumer.actions.heavy_lifting import HeavyLifting, HeavyLiftingRequest
from consumer.bootstrap.container import ConsumerContainer
from consumer.bootstrap.heavy_lifting_request import HeavyLiftingTask

logger = logging.getLogger(__name__)

consumer_container = ConsumerContainer()
consumer_container.wire(modules=[__name__])
celery = consumer_container.celery()


@celery.task(
    base=HeavyLiftingTask,
    name="test.send_message",
    bind=True,
    autoretry_for=(ValueError,),
    retry_kwargs={"max_retries": 5, "countdown": 2},
)
@inject
def run_heavy_lifting(
    self,
    data: str,
    heavy_lifting: HeavyLifting = Provide[
        ConsumerContainer.heavy_lifting_action
    ],
) -> None:
    input_ = HeavyLiftingRequest(message=data)
    heavy_lifting(data=input_)
