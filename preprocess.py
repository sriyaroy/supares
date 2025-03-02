import os
import cv2

# Check dims of an image and if width is >700, proportionally downsample till 700 or under using openCV
def dimCheck(image_path):
    image = cv2.imread(image_path)
    height, width = image.shape[:2]
    if width > 700:
        scale_percent = 700/width
        width = int(width * scale_percent)
        height = int(height * scale_percent)
        dim = (width, height)
        image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

    return image

def dummy_greyscale(image, img_path: str) -> str:
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ouptut_path = os.path.splitext(img_path)[0] + "_grey.jpg"
    cv2.imwrite(ouptut_path, gray_img)
    return ouptut_path
