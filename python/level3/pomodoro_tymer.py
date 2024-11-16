import tkinter as tk # para cear UI
from tkinter.constants import *
import time # para manejar el tiempo

def counter(num):
    current_number.set(current_number.get() + num) # current_number se define más abajo

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60) # divmode convierte segundos a minutos y segundos
        timer = f"{mins:02d}:{secs:02d}" # formatear el timer MM:SS
        print(timer, end="\r") # se imprime el timer en la misma linea
        time.sleep(1) # esperar un segundo
        seconds -= 1
    
    print("Time's up")

# crear la ventana principal
root = tk.Tk()
root.title("Pomodoro tymer") # agregar titulo a la ventana
root.geometry("300x200") # agregar un ancho y alto

current_number = tk.IntVar(value=0) # construir una nueva variable integer

# crear el label para desplegar
number_label = tk.Label(root, textvariable=current_number, font=("Arial", 24))
number_label.pack(pady=20) # pack permite añadir algunos atributos extra, en este caso agrego un padding

# creo un frame para contener los botones al fondo
button_frame = tk.Frame(root)
button_frame.pack(side="bottom", pady=40)

middle_frame = tk.Frame(root)
middle_frame.pack(pady=40)

# crear un input field
entry = tk.Entry(middle_frame, font=("Arial", 24))
entry.pack(pady=10)

# botones
##################### siempre agrego al inicio lo que sería el PARENT, en este caso, button_frame
btn_start = tk.Button(button_frame, text="Start", command=lambda: counter(1))
btn_pause = tk.Button(button_frame, text="Pause", command=lambda: counter(-1))
btn_reset = tk.Button(button_frame, text="Reset", command=lambda: counter(2))

# darle algo de estilo a los botones
btn_start.pack(side="left", padx=5)
btn_pause.pack(side="left", padx=5)
btn_reset.pack(side="left", padx=5)

# iniciar el loop del GUI
root.mainloop()