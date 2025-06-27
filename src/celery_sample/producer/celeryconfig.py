from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CeleryConfig:
    broker_url: str = "pyamqp://guest:guest@172.20.0.4:5672//"
    result_backend: str = (
        "redis://aboba:RvPtXZyLRxRd7zvj3mieYvXAQAQH9Cjw@172.20.0.3:6379/0"
    )

    task_serializer: str = "json"
    result_serializer: str = "json"
    accept_content: list[str] = ["json"]  # noqa:RUF008
    timezone: str = "UTC"
    enable_utc: bool = True
