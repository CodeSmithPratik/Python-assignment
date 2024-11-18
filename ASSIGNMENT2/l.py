import tkinter as tk
from tkinter import messagebox, simpledialog

class Library:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("500x500")
        self.root.config(bg="#F5F5DC")
        self.books = ["Python Programming", "Data Science Handbook", "Machine Learning", "Artificial Intelligence"]

        # Title Label
        self.title_label = tk.Label(root, text="Library Management System", font=("Arial", 18, "bold"), bg="#F5F5DC", fg="#4B0082")
        self.title_label.pack(pady=10)

        # Display Area
        self.display_area = tk.Text(root, height=10, width=50, bg="#FFFACD", fg="#4B0082", font=("Arial", 12))
        self.display_area.pack(pady=10)
        self.display_books()

        # Input Entry
        self.entry_label = tk.Label(root, text="Enter Book Name:", font=("Arial", 12), bg="#F5F5DC", fg="#4B0082")
        self.entry_label.pack(pady=5)
        self.entry = tk.Entry(root, width=40, font=("Arial", 12))
        self.entry.pack(pady=5)

        # Buttons
        self.add_button = tk.Button(root, text="Add Book", width=15, command=self.add_book, bg="#ADD8E6", fg="#4B0082")
        self.add_button.pack(pady=5)

        self.borrow_button = tk.Button(root, text="Borrow Book", width=15, command=self.borrow_book, bg="#ADD8E6", fg="#4B0082")
        self.borrow_button.pack(pady=5)

        self.return_button = tk.Button(root, text="Return Book", width=15, command=self.return_book, bg="#ADD8E6", fg="#4B0082")
        self.return_button.pack(pady=5)

        self.search_button = tk.Button(root, text="Search Book", width=15, command=self.search_book, bg="#ADD8E6", fg="#4B0082")
        self.search_button.pack(pady=5)

        self.display_button = tk.Button(root, text="Display Books", width=15, command=self.display_books, bg="#ADD8E6", fg="#4B0082")
        self.display_button.pack(pady=5)

    def add_book(self):
        book_name = self.entry.get().strip()
        if book_name:
            if book_name not in self.books:
                self.books.append(book_name)
                messagebox.showinfo("Success", f"'{book_name}' has been added to the library.")
            else:
                messagebox.showwarning("Warning", f"'{book_name}' is already in the library.")
            self.entry.delete(0, tk.END)
            self.display_books()
        else:
            messagebox.showwarning("Input Error", "Please enter a book name.")

    def display_books(self):
        self.display_area.delete(1.0, tk.END)
        if self.books:
            self.display_area.insert(tk.END, "Available Books in the Library:\n")
            for book in self.books:
                self.display_area.insert(tk.END, f" - {book}\n")
        else:
            self.display_area.insert(tk.END, "No books are available in the library.")

    def borrow_book(self):
        book_name = self.entry.get().strip()
        if book_name in self.books:
            self.books.remove(book_name)
            messagebox.showinfo("Success", f"You have borrowed '{book_name}'.")
            self.entry.delete(0, tk.END)
            self.display_books()
        else:
            messagebox.showwarning("Unavailable", f"'{book_name}' is not available in the library or has already been borrowed.")

    def return_book(self):
        book_name = self.entry.get().strip()
        if book_name:
            if book_name not in self.books:
                self.books.append(book_name)
                messagebox.showinfo("Success", f"'{book_name}' has been returned to the library.")
            else:
                messagebox.showwarning("Warning", f"'{book_name}' is already in the library.")
            self.entry.delete(0, tk.END)
            self.display_books()
        else:
            messagebox.showwarning("Input Error", "Please enter a book name.")

    def search_book(self):
        book_name = self.entry.get().strip()
        if book_name:
            if book_name in self.books:
                messagebox.showinfo("Found", f"'{book_name}' is available in the library.")
            else:
                messagebox.showinfo("Not Found", f"'{book_name}' is not available in the library.")
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a book name.")

# Create the main window and run the app
root = tk.Tk()
library_app = Library(root)
root.mainloop()
