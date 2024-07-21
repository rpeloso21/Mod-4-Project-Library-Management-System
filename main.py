from classes import *
from operations import *

user1 = User("Tom Sawyer", "111")

books = {}
books["1234"] = Book("The Name of the Wind", "Patrick Roghfus", "1234", "11.22.1990")
users = [user1]
authors = []
genres = []

current_user = None

def main():
    first_run = True
    while True:
        if first_run:
            print("\nWelcome to the library book management system!\n")
            user_id_input = input("Please enter your user ID (hint: '111'): ")
            if user_id_input not in (user.get_id() for user in users):
                print("I'm sorry, that is not a valid user ID.  Please try another ID.")
                continue
            for user in users:
                if user_id_input == user.get_id():
                    print(f"\nWelcome {user.get_name()}.")
                    current_user = user
        first_run = False
        

        print("\nMain Menu: \n1. Book Operations \n2. User Operations \n3. Author Operations \n4. Genre Operations \n5. Change User \n6. Exit")
        operation_input = input("Please make a seletion: ")
        if operation_input == "1":
            book_operations(current_user, users)

        elif operation_input == "2":
            user_operations(current_user, users)

        elif operation_input == "3":
            author_operations(authors)

        elif operation_input == "4":
            genre_operations(genres)

        elif operation_input == "5":

            #need to figure this out!

            if not change_user(current_user, users):
                continue
            else:
                current_user = change_user(current_user, users)

        elif operation_input == "6":
            break            

        else:
            print("That is not a valid selection.  Please try again.")





if __name__ == "__main__":
    main()
                

