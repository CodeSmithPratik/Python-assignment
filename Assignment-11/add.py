import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Addition Program")
root.geometry("300x200")

def add_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

label1 = tk.Label(root, text="Enter first number:")
label1.pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

label2 = tk.Label(root, text="Enter second number:")
label2.pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

add_button = tk.Button(root, text="Add", command=add_numbers)
add_button.pack(pady=10)

result_label = tk.Label(root, text="Result:")
result_label.pack(pady=5)

root.mainloop()
