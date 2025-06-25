from typing import Annotated

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

from producer.actions.send_message import SendMessage, SendMessageRequest
from producer.bootstrap.containers import Container

producer_router = APIRouter(prefix="/produce")


class ProducerRouterPost(BaseModel):
    message: str = Field(default="None message provided", alias="message")


@producer_router.post("/")
@inject
async def post_message(
    request: ProducerRouterPost,
    action: Annotated[SendMessage, Depends(Provide[Container.send_message])],
) -> JSONResponse:
    message = SendMessageRequest(message=request.message)
    task_id = action(data=message)

    return JSONResponse(content={"task_id": task_id}, status_code=202)
