from PIL import Image
import pytesseract

from File_control import write

def change(pictureAddress):
    imgAddr = Image.open(pictureAddress)
    text = pytesseract.image_to_string(imgAddr)
    write(text)
    return text