from urllib.request import urlopen
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

def download_img(url):
    img = urlopen(url)
    with open("userimg.png", "wb") as file:
        file.write(img.read())

def open_img(url_entry, img_label, shared_data):
    url = url_entry.get()
    if url:
        try:
            print("Downloading image...")
            download_img(url)

            print("Opening image...")
            original_img = Image.open("userimg.png")
            original_img.thumbnail((400, 400))
            shared_data["thumbnail"] = original_img
            user_img_tk = ImageTk.PhotoImage(original_img)
            img_label.config(image=user_img_tk)
            img_label.image = user_img_tk
            print("Image opened!")
        except:
            print("Error opening image.")

def on_click(event, C, shared_data):
    C.delete("color_text")
    thumbnail_img = shared_data.get("thumbnail")
    if thumbnail_img is None:
        print("Something didn't work...")
    
    x, y = event.x, event.y
    width, height = thumbnail_img.size
    if 0 <= x < width and 0 <= y < height:
        color = thumbnail_img.getpixel((x, y))
    hex_color = "#%02x%02x%02x" % color
    r_color, g_color, b_color = color
    C.create_rectangle(50,20,250,220, fill = hex_color)
    C.create_text(150, 250, text= hex_color, fill="black", font=('Helvetica 10'), tag = "color_text")
    C.create_text(150, 275, text= f"({r_color}, {g_color}, {b_color})", fill="black", font=('Helvetica 10'), tag = "color_text")

def main():
    root = tk.Tk()
    root.title("Color Picker")
    C = Canvas(root, bg = "white", height = 300, width = 300)
    C.pack()
    text  = tk.Label(root, text = "Paste the URL of the image you wish to color pick from: ")
    text.pack()
    url_entry = tk.Entry(root, width = 50)
    url_entry.pack(pady = 5)
    shared_data = {}
    open_button = tk.Button(root, text = "Open", command = lambda: open_img(url_entry, img_label, shared_data))
    open_button.pack(pady = 5)
    img_label = tk.Label(root)
    img_label.pack(pady = 5, fill = "none", expand = True)
    img_label.bind("<Button-1>", lambda e: on_click(e, C, shared_data))

    root.mainloop()


if __name__ == "__main__":
    main()