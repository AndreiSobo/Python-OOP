# Python Object Oriented Programming by Joe Marini course example
# Using composition to build complex objects


class Book:
    def __init__(self, title, price, author = None):
        self.title = title
        self.price = price

        self.author = author

        self.chapters = []

    def addchapter(self, chapter):
        self.chapters.append(chapter)

    def getBookPageCount(self):
        count = 0
        for chapter in self.chapters:
            count = count + chapter.pagecount
        return count

class Author:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
class Chapter:
    def __init__(self, name, pagecount):
        self.name = name
        self.pagecount = pagecount

a1 = Author("Lev", "Tolstoy")
b1 = Book("War and peace", 22.88, a1)
print(b1.author)
c1 = Chapter("chapter 1", 223)



# b1 = Book("War and Peace", 39.0, "Leo", "Tolstoy")

b1.addchapter(c1)
b1.addchapter(Chapter("Chapter 2", 97))
# b1.addchapter("Chapter 3", 143)

print(b1.title)
print("\n")
print(b1.getBookPageCount())
