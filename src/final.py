from urllib.request import urlopen
import tkinter as tk
from PIL import Image, ImageTk

def download_img(url):
    img = urlopen(url)
    with open("userimg.png", "wb") as file:
        file.write(img.read())

def open_img():
    url = url_entry.get()
    if url and download_img(url):
        img = Image.open("userimg.png")
        img.thumbnail((400,400))
        img_tk = ImageTk.PhotoImage(img)

        img_label.config(image = img_tk)
        img_label.image = img_tk

root = tk.Tk()
root.title("Color Picker")
tk.Label(root, text = "Paste the URL of the image you wish to color pick from: ")
url_entry = tk.Entry(root, width = 50)
open_button = tk.Button(root, text = "Open", command = open_img)
img_label = tk.Label(root)
root.mainloop()
