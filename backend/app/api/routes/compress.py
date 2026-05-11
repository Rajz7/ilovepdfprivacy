from fastapi import FastAPI

app = FastAPI()

@app.get("/compress-pdf")
def compress_pdf():
    pass