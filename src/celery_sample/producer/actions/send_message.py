from dataclasses import dataclass

from celery import Celery, result


@dataclass(frozen=True, slots=True)
class IOBoundRequest:
    message: str


class IOBound:
    def __init__(self, celery: Celery) -> None:
        self._celery = celery

    async def __call__(self, data: IOBoundRequest) -> str:
        task: result.AsyncResult = self._celery.send_task(
            "test.io_bound",
            kwargs={"data": data.message},
        )
        return task.id
