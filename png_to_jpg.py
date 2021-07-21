import tkinter as tk
from tkinter import filedialog
from PIL import Image

root = tk.Tk()
root.title("PNG Convertion Tool To JPG")

canvas = tk.Canvas(root, width=300, height=200, bg='#3664a8', relief='groove')
canvas.pack()

label = tk.Label(root, text='PNG Conversion To JPG', bg='#3664a8')
label.config(font=('roboto', 20))

canvas.create_window(150, 50, window=label)


def get_png():
        global im

        import_file_path = filedialog.askopenfilename()
        im = Image.open(import_file_path)


browseButton_PNG = tk.Button(text='import PNG File', command=get_png, bg='royalblue', fg='white', font=('roboto', 14, 'bold'))

canvas.create_window(150, 100, window=browseButton_PNG)


def convert_jpg():
        global im

        export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg')
        im.save(export_file_path)


saveAsButton_JPG = tk.Button(text='Convert To JPG', command=convert_jpg, bg='royalblue', fg='white', font=('roboto', 14, 'bold'))

canvas.create_window(150, 150, window=saveAsButton_JPG)


root.mainloop()