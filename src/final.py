from urllib.request import urlopen
import PySimpleGUI as sg
from PIL import Image, ImageTk
import io

def download_img(url):
    img = urlopen(url)
    with open("userimg.png", "wb") as file:
        file.write(img.read())

layout = [
    [sg.Text("Paste the URL of the image you wish to color pick from: ")],
    [sg.InputText(key="url_input")],
    [sg.Image(filename="", key="userimg")],
    [sg.Button("Done")]
]

window = sg.Window("Color Picker", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    
    if event == "Done":
        url = values["url_input"]
        if url:
            download_img(url)

            image = Image.open("userimg.png")
            image.thumbnail((400, 400))
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            window["userimg"].update(data=bio.getvalue())

window.close()
