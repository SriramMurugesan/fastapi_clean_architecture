from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    """Root endpoint that returns API information."""
    return {
        "message": "Welcome to FastAPI Clean Architecture",
        "version": "1.0.0",
        "status": "operational"
    }
