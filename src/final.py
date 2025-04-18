from urllib.request import urlopen
import tkinter as tk
from PIL import Image, ImageTk
import pyautogui

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
            user_img.thumbnail((400, 400))
            user_img_tk = ImageTk.PhotoImage(user_img)
            img_label.config(image=user_img_tk)
            img_label.image = user_img_tk
            print("Image opened!")
        except:
            print("Error opening image.")

def on_click(event):
    x, y = event.x, event.y
    print(f"You clicked on ({x}, {y})")
    mouse_click = (x,y)

def find_color(pos):
        x, y = pos  
        img = Image.open("userimg.png")
        color = img.getpixel((x, y))
        print(f"The color is {color}.")
        return color

def main():
    root = tk.Tk()
    root.title("Color Picker")
    tk.Label(root, text = "Paste the URL of the image you wish to color pick from: ")
    url_entry = tk.Entry(root, width = 50)
    url_entry.pack(pady = 5)
    img_label = tk.Label(root)
    img_label.pack(pady = 5, fill = "both", expand = True)
    img_label.bind("<Button-1>", on_click)
    open_button = tk.Button(root, text = "Open", command = lambda: open_img(url_entry, img_label))
    open_button.pack(pady = 5)

    if pyautogui.mouseDown():
        mouse_pos = on_click()
        selected_color = find_color(mouse_pos)
        print(f"Your selected color is {selected_color}.")
    
    root.mainloop()


if __name__ == "__main__":
    main()