# Python Object Oriented Programming by Joe Marini course example
# Using data classes to represent data objects
from dataclasses import dataclass

@dataclass
class Book:
    title : str
    author : str
    pages : int
    price : float

    def bookinfo(self):
        return f"{self.title} by {self.author}. "
    
    def __lt__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Both objects must belong to Book class")
        return (self.price < value.price)


# create some instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)

# access fields
print(b1.title)
print(b2.author)
print("\n")


# TODO: print the book itself - dataclasses implement __repr__
print(b1)

# TODO: comparing two dataclasses - they implement __eq__
print(b1==b3)
print(b3>b1)

# TODO: change some fields
b4 = Book("introduction to java", "john lewes", 500, 39.99)
print(b4.bookinfo())