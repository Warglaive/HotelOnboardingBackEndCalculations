# Dependency Injection and configuration file
from fastapi import FastAPI

from container import ApplicationContainer
from infrastructure.api import todo_controller


def setup(app: FastAPI, container: ApplicationContainer) -> None:

    # Add other controllers here
    app.include_router(todo_controller.router)

    # Inject dependencies
    container.wire(
        modules=[
            todo_controller,
        ]
    )
