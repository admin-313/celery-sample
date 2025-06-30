import logging
import secrets
from dataclasses import dataclass

from celery import Celery

logger = logging.getLogger(__name__)


@dataclass(frozen=True, slots=True)
class CPUHeavyLiftingRequest:
    message: str


class CPUHeavyLifting:
    def __init__(self, celery: Celery) -> None:
        self._celery = celery

    def __call__(self, data: CPUHeavyLiftingRequest) -> None:
        self._fib(36)
        self._fail_randomly()
        logger.info(f"The job {data.message} has been succedeed")  # noqa: G004

    def _fib(self, n: int) -> int:
     if n <= 1:
         return n
     return self._fib(n - 1) + self._fib(n - 2)


    def _fail_randomly(self) -> None:
        if secrets.randbelow(exclusive_upper_bound=2) == 1:
            logger.info("Better luck next time")
            msg = "skill issue"
            raise ValueError(msg)
