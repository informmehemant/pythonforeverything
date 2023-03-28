class ClassTest:
    def instance_method(self):
        print(f"called instance_method of {self}")
    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")
    @staticmethod
    def static_method():
        print("called static_method.")

test = ClassTest()
test.instance_method()
#  in class method, when ClassTest is called , it adds ClassTest.class_method(cls)
ClassTest.class_method()
# class method is used as factory example
# in static method it does not add any thing
ClassTest.static_method()


class Book:
    TYPES = ("hardcover","paperback")
    def __init__(self, name, book_type,weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}>"
    @classmethod
    def handcover(cls,name,page_weight):
        # return Book(name, Book.TYPES[0], page_weight + 100)
        return cls(name, Book.TYPES[0], page_weight + 100)


book = Book.handcover("Harry Potter", 1500)
light = Book.handcover("Harry Potter", 600)  

# book = Book("Harry Potter","hardcover", 1500)

print(book)
print(light)


