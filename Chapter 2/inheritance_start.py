# Python Object Oriented Programming by Joe Marini course example
# Understanding class inheritance
class Publication:
    def __init__(self, title, price):
        self. title = title
        self.price = price

class Book(Publication):
    def __init__(self,title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages

class Periodical(Publication):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price)
        self.publisher = publisher
        self.period = period

class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)

class Newspaper(Periodical):
    def __init__(self,title, publisher, price, period):
        super().__init__(title, publisher, price, period)


b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
n1 = Newspaper("NY Times", "New York Times Company", 6.0, "Daily")
m1 = Magazine("Scientific American", "Springer Nature", 5.99, "Monthly")

print("the b1 author is: ", b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)
print(vars(m1))
