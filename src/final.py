from urllib.request import urlopen
from PIL import Image

    
url = input("Paste the URL of the image you wish to color pick from: ")
img = urlopen(url)
with open ("userimg.png", "wb") as file:
    file.write(img.read())