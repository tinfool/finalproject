from urllib.request import urlopen
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

def download_img(url):
    img = urlopen(url)
    with open("userimg.png", "wb") as file:
        file.write(img.read())

def open_img(url_entry, img_label):
    url = url_entry.get()
    if url:
        try:
            print("Downloading image...")
            download_img(url)
            print("Opening image...")
            user_img = Image.open("userimg.png")
            show_image(user_img, img_label)
        except:
            print("Error opening image.")

def show_image(user_img, img_label):
    user_img_tk = ImageTk.PhotoImage(user_img)
    img_label.config(image=user_img_tk)
    img_label.image = user_img_tk
    print("Image opened!")

            

def on_click(event, C):
    x, y = event.x, event.y
    color = user_img.getpixel((x, y))
    print(f"Color: {color}")
    print(f"x: {x} y: {y}")
    hex_color = "#%02x%02x%02x" % color
    C.config(bg = hex_color)


def main():
    root = tk.Tk()
    root.title("Color Picker")
    C = Canvas(root, bg = "white", height = 300, width = 300)
    C.pack()
    text  = tk.Label(root, text = "Paste the URL of the image you wish to color pick from: ")
    text.pack()
    url_entry = tk.Entry(root, width = 50)
    url_entry.pack(pady = 5)
    img_label = tk.Label(root)
    img_label.pack(pady = 5, fill = "none", expand = True)
    img_label.bind("<Button-1>", lambda e: on_click(e, C))
    open_button = tk.Button(root, text = "Open", command = lambda: open_img(url_entry, img_label))
    open_button.pack(pady = 5)

    root.mainloop()


if __name__ == "__main__":
    main()