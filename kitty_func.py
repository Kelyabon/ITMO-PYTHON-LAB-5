import tkinter as tk
from tkinter import messagebox

from bs4 import BeautifulSoup
import requests
from PIL import Image, ImageTk


def get_kitty():
    window = tk.Tk()
    monitor_height = window.winfo_screenheight()
    monitor_width = window.winfo_screenwidth()

    cat = requests.get('https://aws.random.cat')
    if cat.status_code == 200:
        path = "image.png"
        soup = BeautifulSoup(cat.content, 'lxml')
        photo_link = soup.a.img.get('src')

        image = requests.get(photo_link)
        out = open(path, "wb")
        out.write(image.content)
        out.close()
        title = 'Kitty'
    else:
        title = f'Error {cat.status_code}'
        path = 'Error.png'

    window.title(title)
    image_size = Image.open(path).size
    width = image_size[0]
    height = image_size[1]
    if width > monitor_width - 50 or height > monitor_height - 50:
        width = int(width / 2)
        height = int(height / 2)
        new_image = Image.open(path).resize((width, height))
        new_image.save(path)
    bg_image = ImageTk.PhotoImage(file=path)
    window.geometry(f'{width}x{height}')
    window.resizable(width=False, height=False)
    label = tk.Label(window, image=bg_image)
    label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    button = tk.Button(text='Новый котик', background='black', foreground='lime', font=('Arial', 15))
    button.place(relx=0.1, rely=0.8)

    def button_pressed(event):
        cat_req = requests.get('https://aws.random.cat')
        if cat_req.status_code == 200:
            new_path = "image.png"
            new_soup = BeautifulSoup(cat_req.content, 'lxml')
            new_photo_link = new_soup.a.img.get('src')

            new_image = requests.get(new_photo_link)
            new_out = open(new_path, "wb")
            new_out.write(new_image.content)
            new_out.close()
            new_title = 'Kitty'
            window.title(new_title)
            new_image_size = Image.open(new_path).size
            new_width = new_image_size[0]
            new_height = new_image_size[1]
            if new_width > monitor_width - 50 or new_height > monitor_height - 50:
                new_width = int(new_width / 2)
                new_height = int(new_height / 2)
                image = Image.open(path).resize((new_width, new_height))
                image.save(path)
            new_bg_image = ImageTk.PhotoImage(file=path)
            window.geometry(f'{new_width}x{new_height}')
            label.configure(image=new_bg_image)
            label.image = new_bg_image
        else:
            messagebox.showerror('Ошибка сервера',
                                 'Извините, котики пока что отдыхают...\nПопробуйте чуточку позже')

    button.bind('<Button-1>', button_pressed)
    window.mainloop()
