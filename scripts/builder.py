#example of builder pattern
#Builder class passed to director; only has methods
class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza() #create instance of Pizza class

    def add_marinara(self):
        self.pizza.ingredients.append('Marinara')

    def add_cheese(self):
        self.pizza.ingredients.append('Cheese')

    def add_onion(self):
        self.pizza.ingredients.append('Onion')

    def add_pepperoni(self):
        self.pizza.ingredients.append('Pepperoni')

    def add_artichoke(self):
        self.pizza.ingredients.append('Artichoke Hearts')

    def get_result(self):
        return self.pizza

#object class, instantiated via builder class init
class Pizza:
    def __init__(self):
        self.ingredients = []
    #add other pizza behaviors here

#Director class that constructs objects with builder methods
class Director:
    def construct(self, builder):
        builder.add_marinara()
        builder.add_cheese()
        builder.add_onion()
        builder.add_pepperoni()
        builder.add_artichoke()
        return builder.get_result()

# Client code
builder = PizzaBuilder()
director = Director()
pizza = director.construct(builder)
print(f"Add to dough and bake: {pizza.ingredients}")