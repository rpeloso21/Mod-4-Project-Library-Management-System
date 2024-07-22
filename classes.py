

class Book:
    def __init__(self, title, author, ISBN, publication_date):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.publication_date = publication_date
        self.availability = True

    
    def borrow_book(self, current_user):
        if self.availability:
            self.availability = False
            current_user.borrowed_books.append(self.title)

            print(f"\n'{self.title}' successfully checked out by {current_user.name}!")

        else:
            print("This book is currently unavailable.")
    
    def return_book(self, users):
        self.availability = True

        for user in users:
            if self.title in user.borrowed_books:
                user.borrowed_books.remove(self.title)

        print(f"'{self.title}' returned successfully.")

    def show_status(self):
        if self.availability:
            return "Available"
        else:
            return "Checked Out"
        

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
    
    def get_borrowed_books(self):
        return self.borrowed_books
        
    def borrow_book(self, book):
        self.borrowed_books.append(book.title)


class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography
    

class Genre:
    def __init__(self, name, description, category):
        self.name = name
        self.description = description
        self.category = category
