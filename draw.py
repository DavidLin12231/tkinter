import tkinter as tk
from PIL import Image

# DON'T EDIT THESE FUNCTIONS
def save_canvas():
    canvas.postscript(file="drawing.ps", colormode="color")
    img = Image.open("drawing.ps")
    img.save("drawing.png", "png")

def paint(event):
    # TO DO

#LAYOUT#
root = tk.Tk()
root.title("Drawing App")

canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack()

#Create a CLEAR and SAVE Button

#This means: Only draw when left mouse is down

