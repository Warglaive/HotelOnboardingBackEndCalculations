from dataclasses import asdict
from typing import Optional

from dependency_injector.wiring import Provide
from fastapi import APIRouter

from application import TodoService
from container import ApplicationContainer
from infrastructure.api.todo_schema import TodoEntrySchema

todo_service: TodoService = Provide[ApplicationContainer.todo_service]

router = APIRouter(
    prefix="/todo",
    tags=["Todo"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=list[TodoEntrySchema])
async def list_todos(search: Optional[str] = None) -> list[TodoEntrySchema]:
    todo_entries = todo_service.get_all(search)
    return [TodoEntrySchema(**asdict(todo_entry)) for todo_entry in todo_entries]


@router.post("/")
async def add_todo(content: str) -> str:
    return todo_service.add_entry(content)
