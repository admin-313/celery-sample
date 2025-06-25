from dataclasses import dataclass

from celery import Celery, result


@dataclass(frozen=True, slots=True)
class SendMessageRequest:
    message: str


class SendMessage:
    def __init__(self, celery: Celery) -> None:
        self._celery = celery

    async def __call__(self, data: SendMessageRequest) -> str:
        task: result.AsyncResult = self._celery.send_task(
            "test.send_message",
            kwargs={"data": data.message},
        )
        return task.id
