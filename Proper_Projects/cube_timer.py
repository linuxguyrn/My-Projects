import customtkinter as tk
from pyTwistyScrambler import scrambler222, scrambler333, scrambler444, pyraminxScrambler, skewbScrambler, squareOneScrambler
import time

app = tk.CTk()
app.title("Cube Timer")
app.geometry("600x350")

scramblers = {
    "2x2": scrambler222,
    "3x3": scrambler333,
    "4x4": scrambler444,
    "Pyraminx": pyraminxScrambler,
    "Skewb": skewbScrambler,
    "Square-1": squareOneScrambler
}

timer_running = False
start_time = 0
elapsed_time = 0

def generate_scramble():
    selected_cube = cube_selector.get()
    scrambler = scramblers[selected_cube]
    scramble = scrambler.get_WCA_scramble()
    scramble_label.configure(text=scramble)

def toggle_timer(event):
    global timer_running, start_time, elapsed_time
    if not timer_running:
        timer_running = True
        start_time = time.time()
        update_timer()
    else:
        timer_running = False
        elapsed_time = time.time() - start_time
        timer_label.configure(text=f"Time: {elapsed_time:.2f} seconds")

def update_timer():
    if timer_running:
        elapsed_time = time.time() - start_time
        timer_label.configure(text=f"Time: {elapsed_time:.2f} seconds")
        app.after(10, update_timer) 

cube_selector = tk.CTkComboBox(app, values=list(scramblers.keys()))
cube_selector.set("3x3") 
cube_selector.pack(pady=20)

generate_button = tk.CTkButton(app, text="Generate Scramble", command=generate_scramble)
generate_button.pack(pady=10)

scramble_label = tk.CTkLabel(app, text="", wraplength=550, font=("Algerian", 25))
scramble_label.pack(pady=20)

timer_label = tk.CTkLabel(app, text="Time: 0.00 seconds", font=("Arial", 20))
timer_label.pack(pady=20)

app.bind("<space>", toggle_timer)

app.mainloop()

