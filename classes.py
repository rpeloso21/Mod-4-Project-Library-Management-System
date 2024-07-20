class Book:
    def __init__(self, title, author, ISBN, publication_date):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.publication_date = publication_date
        self.availability = True

    
    def borrow_book(self):
        if self.availability:
            self.availability = False
            print(f"{self.title} sueecessfully checked out!")
        else:
            print("This book is currently unavailable.")
    
    def return_book(self):
        self.availability = True
        print(f"{self.title} returned successfully.")

    def show_status(self):
        if self.availability:
            return "Available"
        else:
            return "Checked Out"


class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography


class User:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        self.borrowed_books = []
        self.borrowing_privileges = "active"
        
    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.ID
        
    def borrow_book(self, book):
        self.borrowed_books.append(book)
    

class Genre:
    def __init__(self, name, description, category):
        self.name = name
        self.description = description
        self.category = category
