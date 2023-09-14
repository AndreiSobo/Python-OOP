# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOKTYPES = ("hardcover", "paperback", "ebook")
    # TODO: double-underscore properties are hidden from other classes

    __booklist = None

    # TODO: create a class method
    @classmethod
    def getBooktypes(cls):
        return cls.BOOKTYPES

    # Book.getBooktypes() is the correct way to access it. We use the class name, followed by the class method. 

    # TODO: create a static method

    @staticmethod
    def getBookList():
        if Book.__booklist == None:
           Book. __booklist = []
        else:
            return Book.__booklist

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def setTitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if booktype not in Book.BOOKTYPES:
            raise ValueError(f"{booktype} is not a valid booktype")
        else:
            self.booktype = booktype


# TODO: access the class attribute
print(Book.getBooktypes())

# TODO: Create some book instances
b1 = Book("Title 1", "ebook")
b2 = Book("Title 2", "ebook")

# TODO: Use the static method to access a singleton object
print("\n")
print(Book.getBookList())
thebooks = Book.getBookList()
thebooks.append(b1)
thebooks.append(b2)
print("\n")
print(Book.getBookList())