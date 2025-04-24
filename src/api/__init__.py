from fastapi import FastAPI
from .root import router as root_router

def register_routes(app: FastAPI) -> None:
    """Register all API routes with the FastAPI application."""
    app.include_router(root_router)
