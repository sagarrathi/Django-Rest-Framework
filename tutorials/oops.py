from typing import List


class Book:
    TYPES=("Hard","Light")

    def __init__(self, name, book_type, weight):
        self.name=name
        self.book_type=book_type
        self.weight=weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type!r}, {self.weight}g>"
    
    def instant_method(self):
        print(f"called instance classe:{self}")
    
    @classmethod
    def hard(cls, name, weight)->"Book":
        return Book(name,Book.TYPES[0],weight+100)

    @classmethod
    def light(cls, name, weight)->"Book":
        return Book(name,Book.TYPES[1],weight)

    @staticmethod
    def static_method():
        print(f"Calling static method")

class SelfHelp(Book):
    def __init__(self, name, book_type, weight,content):
        super().__init__(name, book_type, weight)
        self.content=content

    def __str__(self):
        return f"{super().__str__()}  (Content:{ self.content})"

class BookShelf:
    def __init__(self, books=List[Book]):
        self.books=books
    def __str__(self)->str:
        return f"THis Bookshelf has {len(self.books)} books."


book1=Book.hard("Harry Potter",50)
print(book1)

book2=Book.light("James Bond",50)
print(book2)

book=SelfHelp(name="Jack Reacher", book_type="Hard", weight=120,content="JSKDJSK")
print(book)

shelf=BookShelf([book1, book2, book])
print(shelf)

from pack_unpack import both
print("Where are you", __name__)
both(1,2,3, name="bo")

import sys
print(sys.path)