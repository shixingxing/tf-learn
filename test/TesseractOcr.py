from PIL import Image
import pytesseract

path = "img\\text-img.png"

text = pytesseract.image_to_string(Image.open(path), lang='chi_sim')
print(text)