from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

from producer.actions.send_message import SendMessage, SendMessageRequest

producer_router = APIRouter(prefix="/produce")


class ProducerRouterPost(BaseModel):
    message: str = Field(default="None message provided", alias="message")


@producer_router.post("/")
async def post_message(
    request: ProducerRouterPost,
    action: Annotated[SendMessage, Depends(SendMessage)],
) -> JSONResponse:
    message = SendMessageRequest(message=request.message)
    task_id = action(data=message)

    return JSONResponse(content={"task_id": task_id}, status_code=202)
