from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from PIL import Image, ImageOps
import shutil
import os

app = FastAPI()

def dummy_preprocess(image_path: str) -> str:
    # open image, convert to greyscale and save output
    with Image.open(image_path) as img:
        grey_img = ImageOps.grayscale(img)
        ouptut_path = os.path.splitext(image_path)[0] + "_grey.png"
        grey_img.save(ouptut_path)
    return ouptut_path

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    # save the uploaded file locally
    temp_file_path = os.path.join('uploads', file.filename)
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # preprocess the image
    output_path = dummy_preprocess(temp_file_path)

    return FileResponse(path=output_path, filename='processed.png')