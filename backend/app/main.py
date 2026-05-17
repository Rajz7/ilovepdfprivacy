from fastapi import FastAPI


app = FastAPI(
    title="iLovePDF Privacy API",
    description="A self-hosted version of iLovePDF, with a focus on privacy.",
    version="0.1.0",
)



@app.get("/")
def read_root():
    return {"message": "Welcome to iLovePDF Privacy API"}
