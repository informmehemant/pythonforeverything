# pylint: disable=too-few-public-methods
# pylint: disable=arguments-differ
from abc import ABCMeta, abstractmethod

class IProduct(metaclass=ABCMeta):
    "A Hypothetical Class Interface (Product)"

    @staticmethod
    @abstractmethod
    def create_object():
        "An abstract interface method"

class ConcerteProductA(IProduct):
    "A Concrete Class that implements the Product interface"
    def __init__(self):
        self.name = "ConcreteProductA"
    def create_object(self):
        return self

class ConcreteProductB(IProduct):
    "A Concrete Class that implements the Product interface"
    def __init__(self):
        self.name = "ConcreteProductB"
    def create_object(self):
        return self


class ConcreteProductC(IProduct):
    "A Concrete Class that implements the Product interface"
    def __init__(self):
        self.name = "ConcreteProductC"
    def create_object(self):
        return self

class Creator:
    "The Factory Class"
    @staticmethod
    def create_object(someproperty):
        "A static method to get a concrete product"
        if someproperty == 'a':
            return ConcerteProductA()
        if someproperty == 'b':
            return ConcreteProductB()
        if someproperty == 'c':
            return ConcreteProductC()

# The Client
PRODUCT = Creator.create_object('b')
print(PRODUCT.name)