import asyncio
import logging
from dataclasses import dataclass

from celery import Celery

logger = logging.getLogger(__name__)


@dataclass(frozen=True, slots=True)
class HeavyLiftingRequest:
    message: str


class HeavyLifting:
    def __init__(self, celery: Celery) -> None:
        self._celery = celery

    async def __call__(self, data: HeavyLiftingRequest) -> None:
        await asyncio.sleep(delay=3)
        logger.info(f"The job {data.message} has been succedeed")  # noqa: G004
