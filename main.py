class Book:
    def __init__(self, title, author, ISBN, publication_date):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.publication_date = publication_date
        self.availability = True

class User:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        self.borrowed_books = []
        self.borrowing_privileges = True

    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.ID

class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

class Genre:
    def __init__(self, name, description, category):
        self.name = name
        self.description = description
        self.category = category


user1 = User("Tom Sawyer", "111")

users = [user1]

def main():
    while True:

        current_user = None

        print("\nWelcome to the library book management system!\n")
        user_id_input = input("Please enter your user ID:  ")
        if user_id_input not in (user.get_id() for user in users):
            print("I'm sorry, that is not a valid user ID.  Please try another ID.")
            continue
        for user in users:
            if user_id_input == user.get_id():
                print(f"Welcome {user.get_name()}.")
                current_user = user
        print("\nMain Menu: \n1. Book Operations \n2.User Operations \n3. Author Operations \n4. Genre Operations \n5. Exit \n")






if __name__ == "__main__":
    main()
                

