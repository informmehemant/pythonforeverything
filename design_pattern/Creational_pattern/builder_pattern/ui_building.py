'''
Creational pattern
-Builder pattern (example Layout building )

'''


class LayoutBuilder:
    def __init__(self):
        self.layout = []

    def add_component(self, component):
        self.layout.append(component)
        return self

    def set_alignment(self, alignment):
        for component in self.layout:
            component.set_alignment(alignment)
        return self

    def set_spacing(self, spacing):
        for component in self.layout:
            component.set_spacing(spacing)
        return self

    def build(self):
        return self.layout


# Usage
layout_builder = LayoutBuilder().add_component(
    Button('OK')).add_component(TextField()).set_alignment('center')
