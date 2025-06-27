import logging

from dependency_injector.wiring import Provide, inject

from consumer.actions.heavy_lifting import HeavyLifting, HeavyLiftingRequest
from consumer.bootstrap.container import ConsumerContainer
from consumer.bootstrap.heavy_lifting_request import HeavyLiftingTask

consumer_container = ConsumerContainer()
celery = consumer_container.celery()

logger = logging.getLogger(__name__)


@celery.task(base=HeavyLiftingTask, name="test.send_message")
@inject
def run_heavy_lifting(
    data: str,
    heavy_lifting: HeavyLifting = Provide[
        ConsumerContainer.heavy_lifting_action
    ],
) -> None:
    input_ = HeavyLiftingRequest(message=data)
    heavy_lifting(data=input_)
