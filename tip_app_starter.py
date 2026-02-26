#Incomplete starter code for the Tip App
import tkinter as tk
from tkinter import messagebox

def calculate_tip():
    try:
        bill_amount = float(entry_bill.get())
        tip_amount = float(entry_tippct.get())/100 * bill_amount
        total_amount = bill_amount + tip_amount

        #Update the fields for the Tip and TOTAL
        #YOU DO THIS
        
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid bill amount.")

# Main Window
root = tk.Tk()
root.title("Tip Calculator")
root.geometry("320x300")
root.resizable(False, False)

# Bill Entry
tk.Label(root, text="Enter Bill Amount:").pack(pady=5)
entry_bill = tk.Entry(root)
entry_bill.pack(pady=5)

#Create fields for Tip Button and results
#YOU DO THIS

root.mainloop()
