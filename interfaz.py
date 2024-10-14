import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from PIL import Image, ImageTk
import random
import logica


def main():
    root = tk.Tk()
    root.title("Bienvenido jugador")
    root.geometry('450x450')
    estilo = ttk.Style()
    estilo.configure("TButton", font=('Helvetica', 12), padding=10, relief="flat")
    estilo.configure("TLabel", font=('Helvetica', 12), background='#e0f7fa', padding=10)

    canvas = tk.Canvas(root, width=450, height=450)
    canvas.pack(fill="both", expand=True)

    img = Image.open("imagenes/fondo.png")
    img = img.resize((450, 450))
    background_image = ImageTk.PhotoImage(img)

    canvas.create_image(0, 0, anchor="nw", image=background_image)

    fuente = Font(family="Futuristic", size=15)


    boton_ppt = ttk.Button(root, text="Piedra, Papel o Tijera", command=lambda: logica.ppt())
    boton_palabrasIngles = ttk.Button(root, text="Traducir palabras del inglés", command=lambda: logica.palabrasIngles())
    boton_adivinarNumero = ttk.Button(root, text="Adivina el número", command=lambda: logica.adivinarNumero())

    canvas.create_window(225, 200, anchor="center", window=boton_ppt)
    canvas.create_window(225, 250, anchor="center", window=boton_palabrasIngles)
    canvas.create_window(225, 300, anchor="center", window=boton_adivinarNumero)

    root.background_image = background_image
    root.mainloop()

main()

