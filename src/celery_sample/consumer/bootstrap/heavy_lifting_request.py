import logging

from celery import Task
from celery.worker.request import Request

logger = logging.getLogger(__name__)


class HeavyLiftingRequest(Request):
    def on_failure(
        self,
        exc_info,  # noqa: ANN001
        send_failed_event: bool = True,  # noqa: FBT001, FBT002
        return_ok: bool = False,  # noqa: FBT001, FBT002
    ) -> None:
        super().on_failure(exc_info, send_failed_event, return_ok)
        logger.error("The task %s has been failed", self.task.name)


class HeavyLiftingTask(Task):
    Request = HeavyLiftingRequest
