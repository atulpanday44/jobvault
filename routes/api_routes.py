from fastapi import APIRouter
from models.database_model import Job

router = APIRouter()

@router.get("/jobs")
async def get_jobs():
    # Logic to retrieve jobs
    return [{"id": 1, "title": "Software Engineer"}]
