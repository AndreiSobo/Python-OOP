# Python Object Oriented Programming by Joe Marini course example
# implementing default values in data classes

from dataclasses import dataclass, field
import random

def rndm_prc():
        return float(random.randrange(20, 30))

@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str = "No title"
    author: str = "No author"
    pages: int = 0
    price: float = field(default_factory=rndm_prc)

    

b1 = Book("war and peace", "jamisin", 334)

b2 = Book("war and peace", "jamisin", 334)
b3 = Book("war and peace", "jamisin", 334)
print(b1)
print(b2)
print(b3)