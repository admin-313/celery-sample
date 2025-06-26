import asyncio
import logging
import secrets
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
        self._fail_randomly()
        logger.info(f"The job {data.message} has been succedeed")  # noqa: G004

    def _fail_randomly(self) -> None:
        if secrets.randbelow(exclusive_upper_bound=2) == 1:
            logger.info("Better luck next time")
            msg = "skill issue"
            raise ValueError(msg)
