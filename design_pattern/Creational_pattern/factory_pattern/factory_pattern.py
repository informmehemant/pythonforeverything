'''
abstractions  factory pattern
'''


class UIFactory:
    def create_button(self):
        pass

    def create_textfield(self):
        pass


# concrete factory subclasses for each operating system
# windows subsystem
class WinUIFactory(UIFactory):
    def create_button(self):
        return WinButton()

    def create_textfield(self):
        return WinTextField()


class MacUIFactory(UIFactory):
    def create_button(self):
        return MacOSButton()

    def create_textfield(self):
        return MacOSTextField()

# Abstract product interface


class Button:
    def click(self):
        pass


class TextField:
    def get_text(self):
        pass


# Concrete product subclass for each operating system
class WinButton(Button):
    def click(self):
        print("WinButton clicked")


class WinTextField(TextField):
    def get_text(self):
        return "WinText Field text"


class MacOSButton(Button):
    def click(self):
        print("Mac os Button clicked")


class MacOSTextField(TextField):
    def get_text(self):
        return "Mac os Text Field text"


def create_ui(ui_factory):
    button = ui_factory.create_button()
    textfield = ui_factory.create_textfield()

    button.click()
    print(textfield.get_text())


create_ui(WinUIFactory())
create_ui(MacUIFactory())
