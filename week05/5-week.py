#1 
import typing_extensions
from typing_extensions import Self


class Rectangle:
    def __init__(self,color="green",width=100,height=100,test="test"):
        self.color = color,self.width = width, self.height = height,self.test = test
        
    def square(self):
        return self.width * self.height

rect1 = Rectangle()
print(rect1.color)
print(rect1.square())
print(rect1.test)

rect1 = Rectangle("yellow",23,24)
print(rect1.color)
print(rect1.square())
print(rect1.test)

#2 
import typing_extensions
from typing_extensions import Self


class Name:
    def __init__(self,name="john"):
        self.name = name
        
    def nameFunc(self):
        name = list(name)
        name[0]=name[0].upper()
        print(name)

showName = Name()
print(showName.nameFunc())


showName = Name("almas")
print(showName.nameFunc())

#3
import typing_extensions
from typing_extensions import Self


class Calculator:
    def __init__(self,value1 = 5, value3 = 10):
        self.value1 = value1, self.value2=value3
        
    def multipl(self):
        return self.value1 * self.value2

showResult = Calculator()
print(showResult.multipl())


showResult = Calculator(5,10)
print(showResult.multipl())