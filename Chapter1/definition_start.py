# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Book():

    def __init__(self, name):
        self.name = name
        
    
# TODO: create instances of the class
b1 = Book("book name here")
b2 = Book("war and peace")

# TODO: print the class and property

print(b1)
print(b1.name)
print("\n")
print(vars(b1))