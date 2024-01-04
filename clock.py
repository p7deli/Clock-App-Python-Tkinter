import tkinter as tk
import time
import math
from PIL import Image, ImageTk


def update_clock() -> None:
    
    """
    Update Time Clock
    return : None
    """
    current_time = time.strftime("%H:%M:%S")
    hour, minute, second = time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec
    move_hands(hour, minute, second)
    canvas.delete("txt")
    canvas.create_text(200, 420, text=f"{current_time}", fill="black",
                       font=("Arial", 40, "bold"), tags="txt")
    app.after(1000, update_clock)
    

def move_hands(hour: int, minute: int, second: int) -> None:
    
    """
    move hands clock (hour hand - minute hand - secound hand)
    return: None
    """

    hour_angle = math.radians((hour % 12) * 30 + minute * 0.5)
    minute_angle = math.radians(minute * 6 + second * 0.1)
    second_angle = math.radians(second * 6)
    
    hour_x = center_x + math.sin(hour_angle) * (radius * 0.4)
    hour_y = center_y - math.cos(hour_angle) * (radius * 0.4)
    minute_x = center_x + math.sin(minute_angle) * (radius * 0.6)
    minute_y = center_y - math.cos(minute_angle) * (radius * 0.6)
    second_x = center_x + math.sin(second_angle) * (radius * 0.8)
    second_y = center_y - math.cos(second_angle) * (radius * 0.8)
    
    canvas.delete("hands")
    canvas.create_line(center_x, center_y, hour_x, hour_y, width=8, fill="black", tags="hands")
    canvas.create_line(center_x, center_y, minute_x, minute_y, width=4, fill="black", tags="hands")
    canvas.create_line(center_x, center_y, second_x, second_y, width=2, fill="red", tags="hands")


def draw_numbers() -> None:
    
    """
    Drawing Numbers Clock
    return: none
    """
    
    for i in range(1, 13):
        angle = math.radians(i * 30)
        number_x = center_x + math.sin(angle) * (radius * 0.9)
        number_y = center_y - math.cos(angle) * (radius * 0.9)
        canvas.create_text(number_x, number_y, text=str(i), font=("Arial", 12), fill="black")

# ----------------------------------------- Create Window App

app = tk.Tk()
app.title("clock")

window_width = 400
window_height = 500
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2)) - 20

app.geometry(f"{window_width}x{window_height}+{x}+{y}")
app.config(bg="white")
app.resizable(False, False)

center_x = 200
center_y = 200
radius = 150

# ----------------------- Create picture page
img = Image.open("pictures/ajor.jpg")
img = img.resize((810, 600))
ph = ImageTk.PhotoImage(img)

canvas = tk.Canvas(app, width=410, height=500, bg="#261819")
canvas.place(x=-5, y=0)

canvas.create_image(200, 200, image=ph)
canvas.create_oval(50, 50, 350, 350, fill="white", outline="black", width=8)

draw_numbers()
update_clock()
app.mainloop()