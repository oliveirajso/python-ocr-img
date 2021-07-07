from PIL import Image
import pytesseract
import re

img='imagem.jpeg'
texto =pytesseract.image_to_string(Image.open(img).convert("RGB"), lang='eng')

with open('texto.txt','w') as f:
    f.write(texto)
    f.close()
print(texto)