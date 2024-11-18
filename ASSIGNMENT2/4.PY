import tkinter as tk
from tkinter import messagebox

class Library:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("500x500")
        self.books = ["Python Programming", "Data Science Handbook", "Machine Learning", "Artificial Intelligence"]

        # Title
        tk.Label(root, text="Library Management System", font=("Arial", 18, "bold")).pack(pady=10)

        # Display area for books
        self.display_area = tk.Text(root, height=10, width=50)
        self.display_area.pack(pady=10)
        self.show_books()

        # Book entry
        tk.Label(root, text="Enter Book Name:").pack()
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=5)

        # Buttons
        tk.Button(root, text="Add Book", command=self.add_book).pack(pady=2)
        tk.Button(root, text="Return Book", command=self.return_book).pack(pady=2)
        tk.Button(root, text="Search Book", command=self.search_book).pack(pady=2)
        tk.Button(root, text="Delete Book", command=self.delete_book).pack(pady=2)
        tk.Button(root, text="Show All Books", command=self.show_books).pack(pady=2)

    def add_book(self):
        book = self.entry.get().strip()
        if book and book not in self.books:
            self.books.append(book)
            messagebox.showinfo("Added", f"'{book}' has been added.")
        else:
            messagebox.showwarning("Warning", "Book already in the library or empty input.")
        self.entry.delete(0, tk.END)
        self.show_books()

    def return_book(self):
        book = self.entry.get().strip()
        if book and book not in self.books:
            self.books.append(book)
            messagebox.showinfo("Returned", f"'{book}' has been returned.")
        else:
            messagebox.showwarning("Warning", "Book is already in the library or empty input.")
        self.entry.delete(0, tk.END)
        self.show_books()

    def search_book(self):
        book = self.entry.get().strip()
        if book in self.books:
            messagebox.showinfo("Found", f"'{book}' is available.")
        else:
            messagebox.showinfo("Not Found", f"'{book}' is not in the library.")
        self.entry.delete(0, tk.END)

    def delete_book(self):
        book = self.entry.get().strip()
        if book in self.books:
            self.books.remove(book)
            messagebox.showinfo("Deleted", f"'{book}' has been removed.")
        else:
            messagebox.showwarning("Warning", "Book not found.")
        self.entry.delete(0, tk.END)
        self.show_books()

    def show_books(self):
        self.display_area.delete(1.0, tk.END)
        if self.books:
            self.display_area.insert(tk.END, "Available Books:\n" + "\n".join(self.books))
        else:
            self.display_area.insert(tk.END, "No books available.")

# Run the application
root = tk.Tk()
app = Library(root)
root.mainloop()
