from fastapi import FastAPI
from routes.api_routes import router as api_router

app = FastAPI()

app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "Welcome to Job Vault API"}
