from dataclasses import dataclass
from typing import Any

from celery import Celery


@dataclass(slots=True)
class SendMessageRequest:
    message: str


class SendMessage:
    def __init__(self, celery: Celery) -> None:
        self._celery = celery

    async def __call__(self, data: SendMessageRequest) -> Any:
        task = self._celery.send_task(
            "test.handler", kwargs={"data": data.message},
        )
        return task.id
