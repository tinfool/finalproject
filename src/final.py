from urllib.request import urlopen
import tkinter as tk
from PIL import Image, ImageTk
import pyautogui

class Color():
    def __init__(self, pos):
        self.pos = pos
    
    def find_color(pos):
        # at the pixel's location, find the color   
        print("Your color is... UNKNOWN FOR NOW")

def download_img(url):
    img = urlopen(url)
    with open("userimg.png", "wb") as file:
        file.write(img.read())

def open_img(url_entry):
    url = url_entry.get()
    if url:
        try:
            print("Downloading image...")
            download_img(url)

            print("Opening image...")
            user_img = Image.open("userimg.png")
            user_img.thumbnail((400,400))
            user_img_tk = ImageTk.PhotoImage(img)
            user_img.config(image = user_img_tk)
            user_img.image = user_img_tk
            print("Image opened!")
        except:
            print("Error opening image.")


def main():
    root = tk.Tk()
    root.title("Color Picker")
    tk.Label(root, text = "Paste the URL of the image you wish to color pick from: ")
    url_entry = tk.Entry(root, width = 50)
    url_entry.pack(pady = 5)
    open_button = tk.Button(root, text = "Open", command = open_img(url_entry))
    open_button.pack(pady = 5)
    img_label = tk.Label(root)
    img_label.pack(pady = 5, fill = "both", expand = True)
    root.mainloop()
    mouse_posx, mouse_posy = pyautogui.position()
    print(f"Your mouse is over pixel ({mouse_posx}, {mouse_posy})")
    mouse_click = pyautogui.click()
    selected_color = Color(mouse_click)


if __name__ == "__main__":
    main()