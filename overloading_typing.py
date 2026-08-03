# #SECTİON 6:OVERLOADİNG
#
print("-"*60)
print("Section 6: Overloading Methods")
print("-"*60)

from typing import overload,Union
class Calculator:
    @overload
    def add (self,a:int,b:int) -> int:
        ...
    @overload
    def add (self,a:int,b:int,c:int) -> int:
        ...

    def add (self,a:int,b:int,c:int | None=None) -> int:
        if c is None:
            return a+b
        return a+b+c
    @overload
    def process (self,value:int) -> int:
        ...
    @overload
    def process (self,value:str) -> str:
        ...
    def process (self,value:Union[int,str]) ->  Union[int,str]:
        if isinstance(value,int):
            return value*2
        elif isinstance(value,str):
            return value.upper()
        else:
            raise ValueError("value must be int or str")
calc = Calculator()

print(calc.add(3,4,5))
result=calc.process(5)
print(result)
result = calc.process("ömer")
print(result)
result = calc.process(3.14)
print(result)