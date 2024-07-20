    
from main  import *
from classes import *

def book_operations():

    book_operation_input = input("\nBook Operations \n1. Add a new book \n2. Borrow a book \n3. Return a book \n4. Search for a book \n5. Display all books \nPlease make a selection: ")
    
    if book_operation_input == "1":   #add book
        title = input("What is the title? ")
        author = input("Who is the author? ")
        ISBN = input("Please provide the ISBN: ")
        pub_date = input("Please provide the publication date (mm/dd/yyyy): ")
        books[ISBN] = Book(title, author, ISBN, pub_date)
        print(f"'{books[ISBN].title}' added successfully.")
    
    elif book_operation_input == "2":   #borrow book
        borrow_selection = input("What is the title of the book that you would like to borrow? ")
        for book in books:
            if books[book].title == borrow_selection:
                books[book].borrow_book()
                for user in users:
                    if user.name == current_user:
                        user.borrow_book(book)
            else:
                print("That book is not currently in the library.")
    

    elif book_operation_input == "3":   #return book
        return_selection = input("What is the name of the book that you would like to return? ")
        for book in books:
            if books[book].title == return_selection:
                books[book].return_book()
            else:
                print("That book is not currently in the library.")

    elif book_operation_input == "4":   #search for book
        search_selection = input("What is the name of the book that you would like to search for? ")
        for book in books:
            if books[book].title == search_selection:
                print(f"\n{books[book].title} found. \nStatus: {books[book].show_status()}")
            else:
                print("That book is not currently in the library.")                   

    elif book_operation_input == "5":   #view all books
        for book in books:
            print(f"\nTitle: {books[book].title} \nAuthor: {books[book].author} \nISBN: {books[book].ISBN} \nPublication Date: {books[book].publication_date}")

    else:
        print("That is not a valid selection.  Please try again.")


def user_operations():

    user_operation_input = input("\nUser Operations \n1. Add a new user \n2. View user details \n3. Display all users \nPlease make a selection: ")

    if user_operation_input == "1":   #add a user
        user_name_input = input("What is your name? ")
        user_id_input = input("What is the user ID? ")
        users.append(User(user_name_input, user_id_input))
        print(f"User {user_name_input} created successfully!")


    elif user_operation_input == "2":   #view user details
        view_user_input = input("Please enter the name of the user that you would like to view details on:  \n")
        if view_user_input not in users:
            print("That user was not found.")
        else:
            for user in users:
                if view_user_input == user.name:
                    print(f"User: {user.name} \nID: {user.ID} \nBooks Currently Borrowed: {user.borrowed_books} \nBorrowing Privileges: {user.borrowing_privileges}")
        
    elif user_operation_input == "3":   #view all users
        for user in users:
            print(f"\nUser: {user.name} \nID: {user.ID} \n")

    else:
        print("That is not a valid selection.  Please try again.")


def author_operations():

    author_operation_input = input("\nAuthor Operations \n1. Add a new author \n2. View author details \n3. Display all authors \nPlease make a selection: ")

    if author_operation_input == "1":   #add a author
        author_name_input = input("\nWhat is the autor's name? ")
        author_biography_input = input("Please provide the authors biography: ")
        authors.append(Author(author_name_input, author_biography_input))
        print(f"Author {author_name_input} created successfully!\n")


    elif author_operation_input == "2":   #view autor details
        view_author_input = input("Please enter the name of the author that you would like to view details on:  \n")
        if view_author_input not in authors:
            print("That author was not found.")
        else:
            for author in authors:
                if view_author_input == author.name:
                    print(f"Author: {author.name} \nBiography: {author.biography} \n")

    elif author_operation_input == "3":   #view all users
        for author in authors:
            print(f"\nAuthor: {author.name} \nBiography: {author.biography} \n")

    else:
        print("That is not a valid selection.  Please try again.")



def genre_operations():

    #need to change all author stuff to genre stuff!!!!!

    author_operation_input = input("\nAuthor Operations \n1. Add a new author \n2. View author details \n3. Display all authors \nPlease make a selection: ")

    if author_operation_input == "1":   #add a author
        author_name_input = input("What is the autor's name? ")
        author_biography_input = input("Please provide the authors biography: ")
        authors.append(Author(author_name_input, author_biography_input))
        print(f"User {author_name_input} created successfully!")


    elif author_operation_input == "2":   #view autor details
        view_author_input = input("Please enter the name of the author that you would like to view details on:  \n")
        if view_author_input not in authors:
            print("That author was not found.")
        else:
            for author in authors:
                if view_author_input == author.name:
                    print(f"Author: {author.name} \nBiography: {author.biography} \n")

    elif author_operation_input == "3":   #view all users
        for author in authors:
            print(f"\nAuthor: {author.name} \nBiography: {author.biography} \n")

    else:
        print("That is not a valid selection.  Please try again.")
    

