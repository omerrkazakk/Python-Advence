#DECORATORS
from symtable import Class

print("-"*60)
print("Section 1: Decorators")
print("-"*60)

def my_decorator(func):
    def wrapper():
        print("wrapper function executed")
        func()
        print("wrapper function executed")
    return wrapper

@my_decorator
def hello_world():
    print("hello world")


hello_world()

#PROPERTY DECORATORS
print("-"*60)
print("Section 2: Property Decorators")
print("-"*60)

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        if len(value) < 2:
            print("name is too short")
        else:
            self.__name = value

omer=(Person("Ömer", 20))
print(omer.name)
omer.name="ömer kazak "
print(omer.name)
omer.name="ö"
print(omer.name)

class Car:
    def __init (self ,brand , year):
        self.__brand = brand
        self.__year = year
    @property
    def year(self):
        return self.__year
    @year.setter
    def year(self,value):
        if value<1886:
            print("year is too short")
        else:
            self.__year = value
my_car=Car()
my_car.year=2000
print(my_car.year)
my_car.year=1700
print(my_car.year)

class BankAccount:
    def __init__(self,balance):
        self.__balance = 1000
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self,value):
        if value<0:
            print("Balance cannot be negative")
        else:
            self.__balance = value
my_account=BankAccount(balance=1000)
print(my_account.balance)
my_account.balance=-1000
print(my_account.balance)
my_account.balance=1000
print(my_account.balance)


class User:
    def __init__(self,username,password):
        self.__username=username
        self.__password=password
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self,value):
        if len(value)<3:
            print("username is too short")
        else:
            self.__username = value
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self,value):
        if len(value)<8:
            print("password is too short")
        else:
            self.__password=value
my_information=User("ali","12345678")
my_information.username="öm"
print(my_information.username)
my_information.username="ömer kazak "
print(my_information.username)
my_information.password="1234"
print(my_information.password)
my_information.password="123456789"
print(my_information.password)


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
        if len(value)<3:
            raise ValueError("The name cannot be shorter than 3 characters.")
        else:
            self.__name = value
    @price.setter
    def price(self,value):
        if value<0:
            raise ValueError("The fee cannot be less than 0.")
        else:
            self.__price = value
    @stock.setter
    def stock(self,value):
        if value<0:
            raise ValueError("Stock cannot be less than 0.")
        else:
            self.__stock =value
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