import asyncio

from fastapi import FastAPI

from producer.router import producer_router


async def main() -> None:
    print("Hello from celery-sample!")


if __name__ == "__main__":
    asyncio.run(main())
