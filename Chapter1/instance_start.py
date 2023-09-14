# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title):
        self.title = title
        # TODO: add properties
        

    # TODO: create instance methods
    def addPrice(self, price):
        self.price = price
    
    def getPrice(self):
        return self.price
    
    def addSecret(self, secret):
        self.__secret = secret

    def addDiscount(self, discount):
        self.price = self.price - discount*self.price/100

    #another way of doing this is by making addDiscount just add a self.discount amount, and the getPrice method to modify the price.
    # Best way to do that is as explained in funcitons addDiscount2 and getPrice2
    def addDiscount2(self, amount):
        self._discount = amount

    def getPrice2(self):
        if hasattr(self, "_discount"):
            return self.price -  self._discount * self.price/100
        else:
            return self.price

# TODO: create some book instances
b1 = Book("War and Peace")
b2 = Book("The Catcher in the Rye")
b3 = Book("randomname")
b1.addPrice(22)
b2.addPrice(33.88)
b3.addPrice(50)

# TODO: print the price of book1
print(b1.price)
print(b2.price)
print("\n")
print(b3.getPrice())


# TODO: try setting the discount


print(b3.price)
b3.addDiscount(10)
print(b3.price)
# TODO: properties with double underscores are hidden by the interpreter
b1.addSecret("Cave")
print(vars(b1))
# print(f"b1's secret is: {b1.__secret}")