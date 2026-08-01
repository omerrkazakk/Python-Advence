
class Product:
    def __init__(self,name,price,stock):
        self.__name=name
        self.__price=price
        self.__stock=stock
    @property
    def name(self):
        return self.__name
    @property
    def price(self):
        return self.__price
    @property
    def stock(self):
        return self.__stock
    @name.setter
    def name(self,value):
        if not isinstance(value,str):
            raise TypeError("The name must be a string.")
        if len(value)<3:
            raise ValueError("The name cannot be shorter than 3 characters.")
        else:
            self.__name = value
    @price.setter
    def price(self,value):
        if not isinstance(value,int):
            raise TypeError("The price must be an integer.")
        if value<0:
            raise ValueError("The fee cannot be less than 0.")
        else:
            self.__price = value
    @stock.setter
    def stock(self,value):
        if not isinstance(value,int):
            raise TypeError("The stock must be an integer.")
        if value<0:
            raise ValueError("Stock cannot be less than 0.")
        else:
            self.__stock =value
    @name.deleter
    def name(self):
        self.__name = None
my_product=Product("Notebook",50,20)
my_product.name="Pe"
print(my_product.name)
my_product.price=-100
print(my_product.price)
my_product.stock=-10
print(my_product.stock)
my_product.name="Pencil"
print(my_product.name)
my_product.price=200
print(my_product.price)
my_product.stock=5
print(my_product.stock)
del my_product.name
print(my_product.name)
