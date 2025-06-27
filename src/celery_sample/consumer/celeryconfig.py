from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CeleryConfig:
    broker_url = "pyamqp://guest:guest@172.20.0.4:5672//"
    result_backend = (
        "redis://aboba:RvPtXZyLRxRd7zvj3mieYvXAQAQH9Cjw@172.20.0.3:6379/0"
    )

    task_serializer = "json"
    result_serializer = "json"
    accept_content = ["json"]  # noqa:RUF012
    timezone = "UTC"
    enable_utc = True
