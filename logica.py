import random
import time
import tkinter as tk
from tkinter.font import Font
from tkinter import ttk



def ppt():
    ventana_ppt = tk.Tk()
    ventana_ppt.title("Piedra, Papel o Tijeras")
    ventana_ppt.geometry('300x370')
    ventana_ppt.configure(background='#e0f7fa')

    label01 = ttk.Label(ventana_ppt, text="Elige piedra, papel o tijera:", background='#e0f7fa', padding=10)
    label01.pack(pady=20)

    def jugar(opcionJugador):
        opcionMaquina = random.randint(0, 2)
        opciones = ["piedra", "papel", "tijera"]
        resultadoJuego = ""

        if (opcionJugador == 0 and opcionMaquina == 2) or (opcionJugador == 1 and opcionMaquina == 0) or (
                opcionJugador == 2 and opcionMaquina == 1):
            resultadoJuego = "¡Has ganado!"
        elif opcionJugador == opcionMaquina:
            resultadoJuego = "Empate."
        else:
            resultadoJuego = "Has perdido."

        resultado = f"Tú: {opciones[opcionJugador]} / Máquina: {opciones[opcionMaquina]}\n{resultadoJuego}"
        labelResultado.config(text=resultado)

    def elecciones(eleccion: int):
        jugar(eleccion)

    # Botones de piedra, papel o tijera
    boton_piedra = ttk.Button(ventana_ppt, text="Piedra", command=lambda: elecciones(0))
    boton_piedra.pack(pady=5)

    boton_papel = ttk.Button(ventana_ppt, text="Papel", command=lambda: elecciones(1))
    boton_papel.pack(pady=5)

    boton_tijera = ttk.Button(ventana_ppt, text="Tijera", command=lambda: elecciones(2))
    boton_tijera.pack(pady=5)

    labelResultado = ttk.Label(ventana_ppt, text="", background='#e0f7fa', padding=10)
    labelResultado.pack(pady=20)

    boton_salir = ttk.Button(ventana_ppt, text="Salir", command=ventana_ppt.destroy)
    boton_salir.pack(pady=5)

    ventana_ppt.mainloop()



def palabrasIngles():
    ventana_palabrasIngles = tk.Tk()
    ventana_palabrasIngles.title("Juego de Traducción")
    ventana_palabrasIngles.geometry('300x370')
    ventana_palabrasIngles.configure(background='#eecbff')

    # Diccionario de traducciones
    soluciones = {
        "strawberry": "fresa", "table": "mesa",
        "book": "libro", "chest": "pecho",
        "computer": "ordenador", "phone": "teléfono",
        "window": "ventana", "door": "puerta",
        "car": "coche", "house": "casa",
        "tree": "árbol", "flower": "flor",
        "water": "agua", "food": "comida",
        "friend": "amigo", "family": "familia",
        "finger": "dedo", "city": "ciudad",
        "music": "música", "love": "amor"
    }

    palabras = random.sample(list(soluciones.items()), 5)
    nota = 0
    intento = 0

    def siguiente_palabra():
        # nonlocal sirve para modificar la variable 'i', que se encuentra en una función exterior.
        # global solo puede aplicarse en variables que estén fuera de cualquier función.
        nonlocal intento
        if intento < 5:
            palabra_actual = palabras[intento][0]
            label_palabra.config(text=f"Palabra: {palabra_actual}")
        else:
            label_palabra.config(text="Juego terminado")
            label_resultado.config(text=f"Tu nota final es: {nota}/5")
            boton_comprobar.config(state="disabled")

    def comprobar_traduccion():
        nonlocal intento, nota
        traduccion_actual = palabras[intento][1]
        traduccion = entrada_traduccion.get().strip().lower()

        if traduccion == traduccion_actual:
            label_resultado.config(text=f"¡Correcto! Palabras restantes: {4 - intento}")
            nota += 1
        else:
            label_resultado.config(text=f"¡Incorrecto! Palabras restantes: {4- intento}")

        intento += 1
        siguiente_palabra()


    label_palabra = ttk.Label(ventana_palabrasIngles, text="Traduce:", background='#eecbff', padding=10)
    label_palabra.pack(pady=20)

    entrada_traduccion = ttk.Entry(ventana_palabrasIngles)
    entrada_traduccion.pack(pady=10)

    boton_comprobar = ttk.Button(ventana_palabrasIngles, text="Comprobar", command=comprobar_traduccion)
    boton_comprobar.pack(pady=10)

    label_resultado = ttk.Label(ventana_palabrasIngles, text="", background='#eecbff', padding=10)
    label_resultado.pack(pady=10)

    boton_salir = ttk.Button(ventana_palabrasIngles, text="Salir", command=ventana_palabrasIngles.destroy)
    boton_salir.pack(pady=10)

    siguiente_palabra()
    ventana_palabrasIngles.mainloop()



def adivinarNumero():
    ventana_adivinaNum = tk.Tk()
    ventana_adivinaNum.title("Juego de Adivinanza")
    ventana_adivinaNum.geometry('370x370')
    ventana_adivinaNum.configure(background='#eecbff')

    i = 5
    numero = random.randint(1, 200)

    label01 = ttk.Label(ventana_adivinaNum, text="Adivina el número secreto.", background='#eecbff', padding=10)
    label01.pack(pady=20)

    label02 = ttk.Label(ventana_adivinaNum, text=f"Elige un número del 1 al 200. Intentos restantes: {i}", background='#eecbff')
    label02.pack(pady=20)


    def comprobarNumero():
        nonlocal i
        eleccion = entrada_respuesta.get()

        if not eleccion.isdigit():
            label_comprobacion.config(text="Por favor, ingresa un número válido.")
            return

        eleccion = int(eleccion)

        if eleccion < 1 or eleccion > 200:
            label_comprobacion.config(text="El número debe estar entre el 1 y el 200.")
        elif eleccion > numero:
            i -= 1
            label_comprobacion.config(text=f"El número es menor que {eleccion}. Intentos restantes: {i}")
        elif eleccion < numero:
            i -= 1
            label_comprobacion.config(text=f"El número es mayor que {eleccion}. Intentos restantes: {i}")
        else:
            label_comprobacion.config(text="¡Has acertado!")
            boton_comprobar.config(state="disabled")
            entrada_respuesta.config(state="disabled")


        if i <= 0:
            label_comprobacion.config(text=f"Has agotado los intentos. El número era {numero}")
            boton_comprobar.config(state="disabled")
            entrada_respuesta.config(state="disabled")


    entrada_respuesta = ttk.Entry(ventana_adivinaNum)
    entrada_respuesta.pack(pady=10)

    boton_comprobar = ttk.Button(ventana_adivinaNum, text="Comprobar", command=comprobarNumero)
    boton_comprobar.pack(pady=5)

    label_comprobacion = ttk.Label(ventana_adivinaNum, text="", background='#eecbff')
    label_comprobacion.pack(pady=20)

    boton_salir = ttk.Button(ventana_adivinaNum, text="Salir", command=ventana_adivinaNum.destroy)
    boton_salir.pack(pady=5)

    ventana_adivinaNum.mainloop()