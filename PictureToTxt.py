from PIL import Image
import pytesseract

from File_control import write

def Tchange(pictureAddress, language):
    imgAddr = Image.open(pictureAddress)
    
    text = pytesseract.image_to_string(imgAddr, lang = language)
    write(text)
    return text