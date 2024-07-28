import tkinter as tk
from PIL import Image, ImageTk
import math
from datetime import time, timedelta

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer(initial_count=5):
    count_down(count=initial_count * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count: int):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if len(str(count_sec)) < 2:
        count_sec = "0" + str(count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

new_time = window.after(1000, count_down)

timer_label = tk.Label(window, text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=1)

canvas = tk.Canvas(window, width=205, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = ImageTk.PhotoImage(Image.open("tomato.png"))
canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)

check_mark_label = tk.Label(window, text="✔", fg=GREEN, bg=YELLOW)
check_mark_label.grid(column=1, row=5)

button_start = tk.Button(text="start", bg=YELLOW, highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=4)

button_reset = tk.Button(text="reset", bg=YELLOW, highlightthickness=0)
button_reset.grid(column=3, row=4)

window.mainloop()
