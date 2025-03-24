class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def list_books(self):
        return [book for book in self.books]
class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

library = Library("New York State Library")

book1 = Book("Jungle Book", "J.K Rowling")
book1 = Book("The Invisible Man", "Stephen King")
book1 = Book("Mein Kamph", "Adolf Hitler")

