from classes import *
#  go back and make a single class file and import all from that file.


user1 = User("Tom Sawyer", "111")

books = {}
books["1234"] = Book("The Name of the Wind", "Patrick Roghfus", "1234", "11.22.1990")
users = [user1]
authors = []
genres = []

def main():
    while True:

        current_user = None
        first_run = True
        if first_run:
            print("\nWelcome to the library book management system!\n")
            user_id_input = input("Please enter your user ID:  ")
            if user_id_input not in (user.get_id() for user in users):
                print("I'm sorry, that is not a valid user ID.  Please try another ID.")
                continue
            for user in users:
                if user_id_input == user.get_id():
                    print(f"Welcome {user.get_name()}.")
                    current_user = user
                    first_run = False

        print("\nMain Menu: \n1. Book Operations \n2. User Operations \n3. Author Operations \n4. Genre Operations \n5. Exit")
        operation_input = input("Please make a seletion: ")
        if operation_input == "1":
            book_operation_input = input("\nBook Operations \n1. Add a new book \n2. Borrow a book \n3. Return a book \n4. Search for a book \n5. Display all books \nPlease make a selection: ")
            
            if book_operation_input == "1":
                title = input("What is the title? ")
                author = input("Who is the author? ")
                ISBN = input("Please provide the ISBN: ")
                pub_date = input("Please provide the publication date (mm/dd/yyyy): ")
                books[ISBN] = Book(title, author, ISBN, pub_date)
                print(f"'{books[ISBN].title}' added successfully.")
            
            elif book_operation_input == "2":
                borrow_selection = input("What is the title of the book that you would like to borrow? ")
                for book in books:
                    if books[book].title == borrow_selection:
                        books[book].borrow_book()
                    else:
                        print("That book is not currently in the library.")
            

            elif book_operation_input == "3":
                return_selection = input("What is the name of the book that you would like to return? ")
                for book in books:
                    if books[book].title == return_selection:
                        books[book].return_book()
                    else:
                        print("That book is not currently in the library.")

            elif book_operation_input == "4":
                search_selection = input("What is the name of the book that you would like to search for? ")
                for book in books:
                    if books[book].title == search_selection:
                        print(f"\n{books[book].title} found. \nStatus: {books[book].show_status()}")
                    else:
                        print("That book is not currently in the library.")                   





        elif operation_input == "2":
            user_operation_input = input ("User Operations: \n1. Add new user \n2. View user details \n3. Display all users \nPlease make a selection: ")

        elif operation_input == "3":
            author_operation_input = input ("Author Operations: \n1. Add new author \n2. View author details \n3. Display all authors \n Please make a selection: ")

        elif operation_input == "4":
            genre_operation_input = input ("Genre Operations: \n1. Add new genre \n2. View genre details \n3. Display all genres \n Please make a selection: ")

        elif operation_input == "5":
            break            

        else:
            print("That is not a valid selection.  Please try again.")





if __name__ == "__main__":
    main()
                

