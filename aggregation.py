class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    def add_books(self, book):
        self.books.append(book)
    def list_books(self):
        return [f"{book.name} by {book.author}" for book in self.books]

class Books:
    def __init__(self, name, author):
        self.name = name
        self.author = author

library = Library("National Library of India")        

book1 = Books(name="The Jungle Book", author="J.K Rowling")
book2 = Books(name="I.T", author="Stephen King")
book3 = Books(name="The Invisible Man", author="H.G Wells")

library.add_books(book1)
library.add_books(book2)
library.add_books(book3)

print(library.name)
for book in library.list_books():
    print(book)