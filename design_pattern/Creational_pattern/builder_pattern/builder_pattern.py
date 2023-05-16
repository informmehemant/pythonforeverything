'''
Creational method ,
Builder pattern example
'''


class Pizza:
    def __init__(self):
        self.crust = None
        self.toppings = []

    def add_crust(self, crust):
        self.crust = crust

    def add_topping(self, topping):
        self.toppings.append(topping)

    def __str__(self) -> str:
        return f"A {self.crust} crust pizza with {', '.join(self.toppings)} toppings"

# builder pattern


class PizzaBuilder:
    def __init__(self) -> None:
        self.pizza = Pizza()

    def set_crust(self, crust):
        self.pizza.add_crust(crust)
        return self

    def add_toppings(self, *toppings):
        for topping in toppings:
            self.pizza.add_topping(topping)
        return self

    def get_result(self):
        return self.pizza


builder = PizzaBuilder()
builder.set_crust('thin')
builder.add_toppings("cheese", "pepperoni", "mushroom")
pizza = builder.get_result()
print(pizza)
