# #SECTİON 4:CLASS METHODS
#
print("-"*60)
print("Section 4: Class Methods")
print("-"*60)


class Pizza:
    total_pizzas=0
    def __init__(self,ingredients):
        self.ingredients = ingredients
        Pizza.total_pizzas +=1
    @classmethod
    def margerita(cls):
        return cls(["peynir","domates","fesleğen"])
    @classmethod
    def peperoni(cls):
        return cls(["sucuk","peynir","domates"])
    @classmethod
    def mixed(cls):
        return cls(["peynir","domates","sucuk","fesleğen"])
    @classmethod
    def get_total_pizzas(cls):
        return cls.total_pizzas
pizza1 = Pizza.margerita()
pizza2 = Pizza.peperoni()
pizza3 = Pizza.mixed()
print(pizza1.ingredients)
print(pizza2.ingredients)
print(pizza3.ingredients)
print(Pizza.get_total_pizzas())