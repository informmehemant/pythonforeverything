'''
Factory pattern definations with example
'''

# This is Shape absract class or template class


class Shape:
    def draw(self):
        pass

# subclasses reference from the details


class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle ....")


class Circle(Shape):
    def draw(self):
        print("Drawing a circle")


class ShapeFactory:
    def create_shape(self, shape_type):
        if shape_type == "rectangle":
            return Rectangle()
        elif shape_type == "circle":
            return Circle()
        else:
            raise ValueError(f"Invalid shape type: {shape_type}")


factory = ShapeFactory()
rectangle = factory.create_shape('rectangle')
circle = factory.create_shape('circle')

print(rectangle.draw())

print(circle.draw())
