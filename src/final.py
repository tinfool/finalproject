from urllib.request import urlopen
from PIL import Image

url = input("Paste the URL of the image you wish to color pick from: ")
img = Image.open(urlopen(url))
img.show()