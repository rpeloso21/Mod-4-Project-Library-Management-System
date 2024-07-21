class User:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        self.borrowed_books = []
        self.borrowing_privileges = "active"



user1 = User("tom", "111")

user1.borrowed_books.append("Time Travel")
print(user1.name)
print(user1.borrowed_books)