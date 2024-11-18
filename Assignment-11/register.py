import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Registration Form")
root.geometry("250x200")

fields = ["Name", "Email", "Password"]
entries = {}
for i, field in enumerate(fields):
    tk.Label(root, text=field).grid(row=i, column=0, padx=10, pady=5)
    entries[field] = tk.Entry(root, show="*" if field == "Password" else None)
    entries[field].grid(row=i, column=1)

def register():
    if all(entries[field].get() for field in fields):
        messagebox.showinfo("Success", "Registration Successful!")
    else:
        messagebox.showwarning("Warning", "All fields are required")

tk.Button(root, text="Register", command=register).grid(row=3, columnspan=2, pady=10)

root.mainloop()
