# #SECTİON 3:STATİC METHODS
#
print("-"*60)
print("Section 3: Static Methods")
print("-"*60)

class MathOperations:
    @staticmethod
    def add (x,y):
        return x + y
    @staticmethod
    def divide (x,y):
        return x / y
    @staticmethod
    def subtract (x,y):
        return x-y
    @staticmethod
    def multiply (x,y):
        return x*y

#
# math=MathOperations()
# print(math.add(3,4))
print(MathOperations.add(1,4))
print(MathOperations.divide(10,2))
print(MathOperations.multiply(5,4))
print(MathOperations.subtract(12,3))