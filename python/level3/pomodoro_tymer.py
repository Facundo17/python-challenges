"""
This app uses the Pomodoro technique to help you stay productive by timing work sessions and breaks.

Each Pomodoro session is 25 minutes of focused work, followed by a 5-minute break. 
The user can start, pause, and reset sessions. 
After every four Pomodoros, a longer break of 15 minutes is added.

Use Tkinter to create a simple UI with buttons for starting, pausing, and resetting the timer.
The timer displays the remaining time in MM:SS format.
"""
import tkinter as tk # para cear UI
from tkinter.constants import *

pause = False
original_value = 1500
current_number = 1500
reset = False
nSessions = 0

class MyModalDialog(tk.Toplevel):
    def __init__(self, master, nSessions):
        super().__init__(master)
        self.title("Take a break!")
        self.geometry("300x150")
        self.transient(master)  # Set the main window as the parent
        self.grab_set()         # Make it modal
        self.sessions = nSessions
        
        if self.sessions == 4:
            message = "Take a 15-minute break!"
        else:
            message = "Take a 5-minute break!"

        tk.Label(self, text=message).pack(pady=20)
        tk.Button(self, text="OK", command=self.destroy).pack()

        # Center the modal window relative to its parent (optional)
        self.update_idletasks()
        x = master.winfo_x() + (master.winfo_width() // 2) - (self.winfo_width() // 2)
        y = master.winfo_y() + (master.winfo_height() // 2) - (self.winfo_height() // 2)
        self.geometry(f"+{x}+{y}")

        self.wait_window()  # Wait for this window to be destroyed

def open_modal(nSessions):
    modal = MyModalDialog(root, nSessions)

def start():
    global pause, reset
    
    pause = False
    reset = False
    btn_start.config(state=DISABLED) # desactivo el botón start al inicio
    countdown(current_number) # inicio la cuenta

def pause_button():
    global pause
    
    pause = True

def reset_button():
    global current_number, reset, original_value, nSessions
    
    current_number = original_value
    reset = True
    nSessions = 0
    btn_start.config(state=NORMAL)
    
    number_label.config(text=convert_to_min_seconds(current_number))

def convert_to_min_seconds(min):
    mins, secs = divmod(min, 60)
    return f"{mins:02d}:{secs:02d}"

def countdown(time_left):
    global pause, reset, current_number, nSessions
    
    if reset:
        return
    
    if pause:
        current_number = time_left
        btn_start.config(state=NORMAL)
        return
    
    if time_left > 0:
        timer_text = convert_to_min_seconds(time_left)
        number_label.config(text=timer_text)
        root.after(1000, countdown, time_left - 1)  # Call the function again after 1 second
    else:
        #number_label.config(text="Time's up!")
        nSessions += 1
       
        open_modal(nSessions)  # Open the modal dialog when the timer ends
        
        if nSessions >= 4:
            nSessions = 0
        reset_button() 

# crear la ventana principal
root = tk.Tk()
root.title("Pomodoro tymer") # agregar titulo a la ventana
root.geometry("300x200") # agregar un ancho y alto

#current_number = tk.IntVar(value=1500) # construir una nueva variable integer

# crear el label para desplegar
number_label = tk.Label(root, text="25:00", font=("Arial", 24))
number_label.pack(pady=20) # pack permite añadir algunos atributos extra, en este caso agrego un padding

# creo un frame para contener los botones al fondo
button_frame = tk.Frame(root)
button_frame.pack(side="bottom", pady=40)

middle_frame = tk.Frame(root)
middle_frame.pack(pady=40)

# botones
##################### siempre agrego al inicio lo que sería el PARENT, en este caso, button_frame
btn_start = tk.Button(button_frame, text="Start", command=lambda: start())
btn_pause = tk.Button(button_frame, text="Pause", command=lambda: pause_button())
btn_reset = tk.Button(button_frame, text="Reset", command=lambda: reset_button())

# darle algo de estilo a los botones
btn_start.pack(side="left", padx=5)
btn_pause.pack(side="left", padx=5)
btn_reset.pack(side="left", padx=5)

# iniciar el loop del GUI
root.mainloop()