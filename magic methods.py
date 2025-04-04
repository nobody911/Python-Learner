class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"{self.name} by {self.author} -- {self.pages} pages"
    def __eq__(self, other):
        return self.name == other.name and self.author == other.author
    def __lt__(self, other):
        return f"less than - {self.pages < other.pages}"
    def __gt__(self, other):
        return f"greater than - {self.pages > other.pages}"
    def __add__(self, other):
        return f"{self.pages + other.pages} pages"
    def __contains__(self, keyword):
        return keyword in self.name or keyword in self.author
    def __getitem__(self, key):
        if key.lower() == "name":
            return self.name
        elif key.lower() == "author":
            return self.author
        elif key.lower() == "pages":
            return self.pages
        else:
            return f"Value of {key} not found"

book1 = Book("The Invisible Man", "H.G. Wells", 392)
book2 = Book("Jungle Book", "J.K. Rowling", 470)
book3 = Book("Cindrella", "Charles Perrault", 236)
book4 = Book("The Invisible Man", "H.G. Wells", 100)

print(book1)
print(book2)
print(book3)

# print(book1 == book4)
# print(book1 < book2)
# print(book1>book2)
# print(book1+book2)
# print("Rowling" in book2)
print(book3["author"]) # accessing class attributes by indexing