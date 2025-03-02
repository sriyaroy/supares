from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from PIL import Image, ImageOps
import shutil
import os
import logging
import preprocess

logger = logging.getLogger('SupaRes')
logger.setLevel(logging.INFO)

app = FastAPI()

@app.post("/")
async def upload(file: UploadFile = File(...)):
    logger.info(f"Received file: {file.filename}")
    # save the uploaded file locally
    temp_file_path = os.path.join('uploads', file.filename)
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # preprocess the image
    output_path = preprocess.dummy_preprocess(temp_file_path)
    logger.info(f"Processed file: {output_path}")

    return FileResponse(path=output_path, filename='processed.png')