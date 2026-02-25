import tkinter as tk

def greet():
    name = entry.get()
    label.config(text=f"Hello, {name}!")

root = tk.Tk()
root.title("My GUI")
root.geometry("500x300")
label = tk.Label(root, text="Hello, World", font=("Arial", 24))
label.pack()
button = tk.Button(root, text="Click Here", command=greet)
button.pack()
entry = tk.Entry(root)
entry.pack()
root.mainloop()

