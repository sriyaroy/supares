from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import shutil
import sys
import logging
import preprocess

logger = logging.getLogger('SupaRes')
logger.setLevel(logging.INFO) # Without StreamHandler this doesn't send the logs anywhere

# Attach a StreamHandler to send logs to STDOUT if none exists yet
if not logger.handlers:
    console_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter("%(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

app = FastAPI()

@app.post("/")
async def upload(file: UploadFile = File(...)):
    logger.info(f"Received file: {file.filename}")
    # save the uploaded file locally
    temp_file_path = f"/tmp/{file.filename}"
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # preprocess the image
    output_img = preprocess.dimCheck(temp_file_path)
    output_path = preprocess.dummy_greyscale(output_img, temp_file_path)
    logger.info(f'Sending processed file to user: {output_path}')

    return FileResponse(path=output_path, filename='processed.png')

@app.get("/")
async def index():
    return {"message": "Server Working"}