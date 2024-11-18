import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Simple Tkinter Program")
root.geometry("300x200")

def show_message():
    messagebox.showinfo("Information", "Hello Virat")

button = tk.Button(root, text="Click Me", command=show_message)
button.pack(pady=50)

root.mainloop()
