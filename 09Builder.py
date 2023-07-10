"""
-------------------------------------------------------------------------------
BUILDER Creational Pattern
-------------------------------------------------------------------------------

https://refactoring.guru/design-pattern/builder

BUILDER

We will use an abstract class from which we will inherit the rest of the houses

House,

Mansion, House with swimming pool, Garage house
"""

class Cook:
    '''
    Director - Manages the creation of the object
    '''

    def __init__(self):
        self._builder = None

    def prepare(self, builder):
        self._builder = builder
        self._builder.prepare_dough()
        self._builder.add_extras()
        self._builder.bake()

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def prepare_dough(self):
        pass

    def add_extras(self):
        pass

    def bake(self):
        pass

class MargeritaBuilder(PizzaBuilder):
    '''
    ConcreteBuilder - a specific builder that creates and combines the
    components of the created object
    '''
    def prepare_dough(self): pass

    def add_extras(self):
        print("Adding mozarella, tomato juice, basil etc.")

    def bake(self): pass

class PepperoniBuilder(PizzaBuilder):
    def prepare_dough(self): pass

    def add_extras(self):
        print("Adding pepperoni salami")

    def bake(self): pass

class Pizza:
    '''
    The generated complex object
    '''
    print("A pizza has been instantiated.")

def main():
    cook = Cook()
    # we choose a builder
    pepperoni_builder = PepperoniBuilder()
    cook.prepare(pepperoni_builder)
    pizza = pepperoni_builder.pizza

    return pizza

if __name__ == '__main__':
    main()