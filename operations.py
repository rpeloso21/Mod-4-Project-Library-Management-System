    
from main  import *
from classes import Book, User, Genre
import re

def book_operations(current_user, users):

    book_operation_input = input("\nBook Operations \n1. Add a new book \n2. Borrow a book \n3. Return a book \n4. Search for a book \n5. Display all books \nPlease make a selection: ")
    
    if book_operation_input == "1":   #add book
        title = input("What is the title? ")
        author = input("Who is the author? ")
        ISBN = input("Please provide the ISBN: ")

        while True:
            pub_date = input("Please provide the publication date (mm/dd/yyyy): ")
            if re.match("^(0[1-9]|1[0-2])/([0-2][0-9]|3[01])/\d{4}$", pub_date):
                books[ISBN] = Book(title, author, ISBN, pub_date)
                print(f"\n'{books[ISBN].title}' added successfully.")
                break
            else:
                print("That is not a valid date format.  Please try again.")
    
    elif book_operation_input == "2":   #borrow book
        borrow_selection = input("What is the title of the book that you would like to borrow? ").lower()
        for book in books:
            if books[book].title.lower() == borrow_selection:
                books[book].borrow_book(current_user)
                return
            
        print("\nThat book is not currently in the library.")
    

    elif book_operation_input == "3":   #return book
        return_selection = input("What is the name of the book that you would like to return? ").lower()
        for book in books:
            if books[book].title.lower() == return_selection:
                books[book].return_book(users)
                return
        print("\nThat book is not currently in the library.")

    elif book_operation_input == "4":   #search for book
        search_selection = input("What is the name of the book that you would like to search for? ").lower()
        for book in books:
            if books[book].title.lower() == search_selection:
                print(f"\n{books[book].title} found. \nStatus: {books[book].show_status()}")
                return
        print("That book is not currently in the library.")                   

    elif book_operation_input == "5":   #view all books
        for book in books:
            print(f"\nTitle: {books[book].title} \nAuthor: {books[book].author} \nISBN: {books[book].ISBN} \nPublication Date: {books[book].publication_date}")

    else:
        print("That is not a valid selection.  Please try again.")


def user_operations(current_user, users):

    user_operation_input = input("\nUser Operations \n1. Add a new user \n2. View user details \n3. Display all users \nPlease make a selection: ")

    if user_operation_input == "1":   #add a user
        user_name_input = input("What is your name? ")
        user_id_input = input("What is the user ID? ")
        users.append(User(user_name_input, user_id_input))
        print(f"\nUser '{user_name_input}' created successfully!")


    elif user_operation_input == "2":   #view user details
        view_user_input = input("Please enter the name of the user that you would like to view details on: ").lower()
        if view_user_input not in (user.name.lower() for user in users):
            print("That user was not found.")
        else:
            for user in users:
                if view_user_input == user.name.lower():
                    print(f"\nUser: {user.name} \nID: {user.ID} \nBooks Currently Borrowed: {user.borrowed_books} \nBorrowing Privileges: {user.borrowing_privileges}")
        
    elif user_operation_input == "3":   #view all users
        for user in users:
            print(f"\nUser: {user.name} \nID: {user.ID} \n")

    else:
        print("That is not a valid selection.  Please try again.")


def author_operations(authors):

    author_operation_input = input("\nAuthor Operations \n1. Add a new author \n2. View author details \n3. Display all authors \nPlease make a selection: ")

    if author_operation_input == "1":   #add a author
        author_name_input = input("\nWhat is the autor's name? ")
        author_biography_input = input("Please provide the authors biography: ")
        authors.append(Author(author_name_input, author_biography_input))
        print(f"\nAuthor '{author_name_input}' created successfully!\n")


    elif author_operation_input == "2":   #view autor details
        view_author_input = input("Please enter the name of the author that you would like to view details on: ").lower()
        if view_author_input not in (author.name.lower() for author in authors):
            print("That author was not found.")
        else:
            for author in authors:
                if view_author_input == author.name.lower():
                    print(f"\nAuthor: {author.name} \nBiography: {author.biography} \n")

    elif author_operation_input == "3":   #view all users
        for author in authors:
            print(f"\nAuthor: {author.name} \nBiography: {author.biography} \n")

    else:
        print("That is not a valid selection.  Please try again.")



def genre_operations(genres):

    genre_operation_input = input("\nGenre Operations \n1. Add a new genre \n2. View genre details \n3. Display all genres \nPlease make a selection: ")

    if genre_operation_input == "1":   #add a genre
        genre_name_input = input("\nWhat is the name of the genre? ")
        genre_description_input = input("Please provide a description of the genre: ")
        genre_category_input = input("What category is the genre in? ")
        genres.append(Genre(genre_name_input, genre_description_input, genre_category_input))
        print(f"\nGenre '{genre_name_input}' created successfully!")


    elif genre_operation_input == "2":   #view genre details
        view_genre_input = input("Please enter the name of the genre that you would like to view details on: ").lower()
        if view_genre_input not in (genre.name.lower() for genre in genres):
            print("That genre was not found.")
        else:
            for genre in genres:
                if view_genre_input == genre.name.lower():
                    print(f"\nGenre: {genre.name} \nDescritpion: {genre.description} \nCategory: {genre.category}")

    elif genre_operation_input == "3":   #view all genres
        for genre in genres:
            print(f"\nGenre: {genre.name} \nDescription: {genre.description} \nCategory: {genre.category}")

    else:
        print("That is not a valid selection.  Please try again.")

    
def change_user(current_user, users):
    change_user_input = input("What is the name of the user that you would like to change to? ").lower()

    if change_user_input not in (user.name.lower() for user in users):
        print("That user was not found.")
        return None

    else:
        for user in users:
            if change_user_input == user.name.lower():
                current_user = user
                print(f"\nCurrent user updated to '{user.name}'.")
                return user
    

