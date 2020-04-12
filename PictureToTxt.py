from PIL import Image
import pytesseract

from File_control import write

def Tchange(pictureAddress):
    imgAddr = Image.open(pictureAddress)
    text = pytesseract.image_to_string(imgAddr)
    write(text)
    return text