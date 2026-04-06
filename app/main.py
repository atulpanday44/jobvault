from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust as necessary
    allow_credentials=True,
    allow_methods=["*"],   # Adjust as necessary
    allow_headers=["*"],   # Adjust as necessary
)

# Routes
@app.get("/")
async def read_root():
    return {"message": "Welcome to JobVault!"}

@app.get("/jobs")
async def get_jobs():
    return [{"id": 1, "title": "Software Engineer"}, {"id": 2, "title": "Data Scientist"}]

@app.post("/jobs")
async def create_job(job: dict):
    return {"message": "Job created", "job": job}

@app.delete("/jobs/{job_id}")
async def delete_job(job_id: int):
    return {"message": f"Job {job_id} deleted"}