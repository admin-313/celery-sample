from typing import Annotated

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

from producer.actions.cpu_bound import CPUBound, CPUBoundRequest
from producer.actions.send_message import IOBound, IOBoundRequest
from producer.bootstrap.containers import Container

producer_router = APIRouter(prefix="/produce")


class ProducerRouterPost(BaseModel):
    message: str = Field(default="None message provided", alias="message")


@producer_router.post("/io")
@inject
async def post_message(
    request: ProducerRouterPost,
    action: Annotated[IOBound, Depends(Provide[Container.send_message])],
) -> JSONResponse:
    action_data = IOBoundRequest(message=request.message)
    task_id = await action(data=action_data)

    return JSONResponse(content={"task_id": task_id}, status_code=202)


@producer_router.post("/cpu")
@inject
async def post_cpu_bound(
    request: ProducerRouterPost,
    action: Annotated[CPUBound, Depends(Provide[Container.cpu_bound])],
) -> JSONResponse:
    action_data = CPUBoundRequest(message=request.message)
    task_id = await action(data=action_data)

    return JSONResponse(content={"task_id": task_id}, status_code=202)
