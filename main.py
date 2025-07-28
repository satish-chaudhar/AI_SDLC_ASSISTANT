from fastapi import FastAPI, UploadFile, File
from rag_engine import load_and_embed
import os

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    path = os.path.join("documents", file.filename)
    with open(path, "wb") as f:
        f.write(await file.read())
    vectordb = load_and_embed(path)
    return {"status": "uploaded and embedded"}
