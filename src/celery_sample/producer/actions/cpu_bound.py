from dataclasses import dataclass

from celery import Celery, result


@dataclass(frozen=True, slots=True)
class CPUBoundRequest:
    message: str


class CPUBound:
    def __init__(self, celery: Celery) -> None:
        self._celery = celery

    async def __call__(self, data: CPUBoundRequest) -> str:
        task: result.AsyncResult = self._celery.send_task(
            "test.cpu_bound",
            kwargs={"data": data.message},
        )
        return task.id
