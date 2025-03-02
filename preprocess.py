from PIL import Image, ImageOps
import os

def dummy_preprocess(image_path: str) -> str:
    # open image, convert to greyscale and save output
    with Image.open(image_path) as img:
        grey_img = ImageOps.grayscale(img)
        ouptut_path = os.path.splitext(image_path)[0] + "_grey.png"
        grey_img.save(ouptut_path)
    return ouptut_path

def