from fastapi import FastAPI
from .root import router as root_router
from ..todos.controller import router as todos_router
from ..auth.controller import router as auth_router
from ..users.controller import router as users_router

def register_routes(app: FastAPI) -> None:
    """Register all API routes with the FastAPI application."""
    app.include_router(root_router)
    app.include_router(todos_router)
    app.include_router(auth_router)
    app.include_router(users_router)
