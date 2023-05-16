'''
Widgit creation using factory method

'''


class Widgit:
    def draw(self):
        pass

# subclass reference from the


class Button(Widgit):
    def draw(self):
        print(" button on the screen....")


class TextField(Widgit):
    def draw(self):
        print("Text Field is painted....")


class Checkbox(Widgit):
    def draw(self):
        print("Checkbox on the screen")


class WidgetFactory:
    @staticmethod
    def create_widget(widget_type):
        if widget_type == 'checkbox':
            return Checkbox()
        elif widget_type == 'textfield':
            return TextField()
        elif widget_type == 'button':
            return Button()
        else:
            raise ValueError(f'Invalid widgit_type:{widget_type}')


# factory = WidgetFactory().create_widget('button')
button = WidgetFactory.create_widget('button')
textfield = WidgetFactory.create_widget('textfield')
checkbox = WidgetFactory.create_widget('checkbox')
print(button.draw())
