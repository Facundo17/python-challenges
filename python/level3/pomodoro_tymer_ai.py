import tkinter as tk
import time

def start_countdown():
    try:
        time_left = int(entry.get())
        countdown(time_left)
    except ValueError:
        label.config(text="Enter a valid number!")

def countdown(time_left):
    if time_left > 0:
        mins, secs = divmod(time_left, 60)
        timer_text = f"{mins:02d}:{secs:02d}"
        label.config(text=timer_text)
        root.after(1000, countdown, time_left - 1)  # Call the function again after 1 second
    else:
        label.config(text="Time's up!")

# Create the tkinter window
root = tk.Tk()
root.title("Countdown Timer")

# Create input field
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

# Create start button
start_button = tk.Button(root, text="Start Countdown", command=start_countdown)
start_button.pack(pady=5)

# Create a label to show the countdown
label = tk.Label(root, text="00:00", font=("Arial", 24))
label.pack(pady=20)

# Run the GUI loop
root.mainloop()
