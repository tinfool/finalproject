from urllib.request import urlopen
import tkinter as tk
from PIL import Image, ImageTk

def download_img(url):
    img = urlopen(url)
    with open("userimg.png", "wb") as file:
        file.write(img.read())

def open_img():
    url = url_entry.get()
    if url:
        try:
            print("Downloading image...")
            download_img(url)

            print("Opening image...")
            img = Image.open("userimg.png")
            img.thumbnail((400,400))
            img_tk = ImageTk.PhotoImage(img)
            img_label.config(image = img_tk)
            img_label.image = img_tk
            print("Image opened!")
        except:
            print("Error opening image.")

root = tk.Tk()
root.title("Color Picker")
tk.Label(root, text = "Paste the URL of the image you wish to color pick from: ")
url_entry = tk.Entry(root, width = 50)
url_entry.pack(pady = 5)
open_button = tk.Button(root, text = "Open", command = open_img)
open_button.pack(pady = 5)
img_label = tk.Label(root)
img_label.pack(pady = 5, fill = "both", expand = True)
root.mainloop()
