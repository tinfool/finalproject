from urllib.request import urlopen
import PySimpleGUI as sg
from PIL import Image, ImageTk
import io

def download_img(url):
    img = urlopen(url)
    with open ("userimg.png", "wb") as file:
        file.write(img.read())


layout = [
    [sg.Text("Paste the URL of the image you wish to color pick from: ")],
    [sg.InputText(key = "url_input")],
    [sg.Image(filename = "user_img", key = "image")],
    [sg.Button("Done")]
]

window = sg.Window("Color Picker", layout)