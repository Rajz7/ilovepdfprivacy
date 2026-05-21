import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router


app = FastAPI(
    title="iLovePDF Privacy API",
    description="A self-hosted version of iLovePDF, with a focus on privacy.",
    version="0.1.0",
)


frontend_origins = os.getenv("FRONTEND_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173")
allow_origins = [origin.strip() for origin in frontend_origins.split(",") if origin.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)



@app.get("/")
def read_root():
    return {"message": "Welcome to iLovePDF Privacy API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
