import tkinter as tk
from tkinter import messagebox

class Library:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("500x500")
        self.root.config(bg="#E6E6FA")  # Light lavender background
        self.books = ["Python Programming", "Data Science Handbook", "Machine Learning", "Artificial Intelligence"]

        # Title Label
        self.title_label = tk.Label(root, text="Library Management System", font=("Arial", 18, "bold"), bg="#E6E6FA", fg="#4B0082")
        self.title_label.pack(pady=10)

        # Display Area
        self.display_area = tk.Text(root, height=10, width=50, bg="#FFFACD", fg="#4B0082", font=("Arial", 12))
        self.display_area.pack(pady=10)
        self.display_books()

        # Input Entry
        self.entry_label = tk.Label(root, text="Enter Book Name:", font=("Arial", 12), bg="#E6E6FA", fg="#4B0082")
        self.entry_label.pack(pady=5)
        self.entry = tk.Entry(root, width=40, font=("Arial", 12))
        self.entry.pack(pady=5)

        # Buttons
        self.add_button = tk.Button(root, text="Add Book", width=15, command=self.add_book, bg="#ADD8E6", fg="#4B0082")
        self.add_button.pack(pady=5)

        self.return_button = tk.Button(root, text="Return Book", width=15, command=self.return_book, bg="#ADD8E6", fg="#4B0082")
        self.return_button.pack(pady=5)

        self.search_button = tk.Button(root, text="Search Book", width=15, command=self.search_book, bg="#ADD8E6", fg="#4B0082")
        self.search_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Book", width=15, command=self.delete_book, bg="#ADD8E6", fg="#4B0082")
        self.delete_button.pack(pady=5)

        self.display_button = tk.Button(root, text="Display Books", width=15, command=self.display_books, bg="#ADD8E6", fg="#4B0082")
        self.display_button.pack(pady=5)

    def add_book(self):
        book_name = self.entry.get().strip().lower()
        if book_name:
            if book_name not in map(str.lower, self.books):
                self.books.append(self.entry.get().strip())
                messagebox.showinfo("Success", f"'{self.entry.get()}' has been added to the library.")
            else:
                messagebox.showwarning("Warning", f"'{self.entry.get()}' is already in the library.")
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

    def return_book(self):
        book_name = self.entry.get().strip().lower()
        if book_name:
            if book_name not in map(str.lower, self.books):
                self.books.append(self.entry.get().strip())
                messagebox.showinfo("Success", f"'{self.entry.get()}' has been returned to the library.")
            else:
                messagebox.showwarning("Warning", f"'{self.entry.get()}' is already in the library.")
            self.entry.delete(0, tk.END)
            self.display_books()
        else:
            messagebox.showwarning("Input Error", "Please enter a book name.")

    def search_book(self):
        book_name = self.entry.get().strip().lower()
        found = next((book for book in self.books if book.lower() == book_name), None)
        if found:
            messagebox.showinfo("Found", f"'{found}' is available in the library.")
        else:
            messagebox.showinfo("Not Found", f"'{self.entry.get()}' is not available in the library.")
        self.entry.delete(0, tk.END)

    def delete_book(self):
        book_name = self.entry.get().strip().lower()
        found = next((book for book in self.books if book.lower() == book_name), None)
        if found:
            self.books.remove(found)
            messagebox.showinfo("Deleted", f"'{found}' has been removed from the library.")
            self.entry.delete(0, tk.END)
            self.display_books()
        else:
            messagebox.showwarning("Not Found", f"'{self.entry.get()}' is not available in the library.")

# Create the main window and run the app
root = tk.Tk()
library_app = Library(root)
root.mainloop()
