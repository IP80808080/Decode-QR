import pyzbar.pyzbar as pyzbar
from PIL import Image

def decode(image_path):

    image = Image.open(image_path)
    decoded = pyzbar.decode(image)
    for i in decoded:
        print(i.type)
        print(i.data.decode('utf-8'))


decode("9anime.png")
