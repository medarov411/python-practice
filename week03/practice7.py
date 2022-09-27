#1(1)
def square(d):
    area = d**2
    print(str(area)," area of the Square")
def rectangle(x,y):
    area = x*y
    print(str(area)," area of the Rectangle")

user_input = int(input("choose the geometric shape: 1 - square, 2 - rectangle: "))

if user_input == 1:
    value1 = int(input("enter the value for square: "))
    square(value1)
if user_input == 2:
    width = int(input("enter the width: "))
    height = int(input("enter the height : "))
    rectangle(width,height)
#1(2)
x =[1,2,3,4,5,6,7]
y=[8,9,10,2]
z=[12,34,5,6,7]

f=0

sum = 0
for i in range(len(x)):
    sum += x[i]
    f+=1

print("1-st array arithmetic mean: ", str(sum/f), "sum: ", str(sum))

for i in range(len(y)):
    sum += y[i]
    f+=1

print("1-st array arithmetic mean: ", str(sum/f), "sum: ", str(sum))

for i in range(len(z)):
    sum += z[i]
    f+=1

print("1-st array arithmetic mean: ", str(sum/f), "sum: ", str(sum))

#2(1)
from math import sqrt
def hexagonArea(d) :
    return (3 * sqrt(3) * pow(d, 2)) / 8
d = int(input("enter the value for hexagon: "))
print("Area of hexagon:",round(hexagonArea(d), 3))


#2(2)
def rectangle(x,y):
    area = x*y
    print(str(area*3)," area of the 3 Rectangles")


width = int(input("enter the width: "))
height = int(input("enter the height : "))
rectangle(width,height)

#3(2)
x = [int(input("print element: ")) for i in range(8)]


for i in range(8):
    if x[i] < 15:
        x[i] = x[i] * 2
print(x)

#4(1)
y = int(input("amount of elements: "))
x = [int(input("print element: ")) for i in range(y)]

g = 0
for i in range(y):
    if x[i] > g:
        g = x[i]
print("greatest number",str(g))
print(str(x.index(g,0,len(x)))," - ordinal number")

#4(2)
y = int(input("amount of elements: "))
x = [int(input("print element: ")) for i in range(y)]

z=[]

for i in range(y):
    if x[i]%2==0:
        z.append(x[i])
z.sort()
print(z)  

#5(1)
y = int(input("amount of elements: "))
x = [int(input("print element: ")) for i in range(y)]

z=[]

for i in range(y):
    if x[i]<0:
        print(x[i+1])
    if x[i]==len(x) and x[i]< 0:
        print("no pair next")
#5(2)
x = [1, 21, -13, -9, 4, 21, 4, 0, -7, 78, -61, -45, 53]
y = [*set(x)]
print(y)

#6(1)
a = [1, 21, -13, -9, 4, 4, 0, -7, 78, -61, -45, 53]
less = 0
greater = 0
print('Maximum of the array: ', max(a))
for i in range(len(a)):
    if a[i] < max(a):
        if a[i] > a[i-1]:
            less = a[i]
        else:
            less = a[i-1]
    else:
        if (a[i] > a[i-1]):
            greater = a[i]
            if a[i] == max(a):
                print('There is no element greater than maximum')
        else:
            greater = a[i-1]
            if a[i-1] == max(a):
                print('There is no element greater than maximum')
print('Element less than maximum: ', less)

#6(2)
a = []
n = 10
sum = 0
for i in range(n):
    a.append(int(input('Enter the array elements: ')))
for i in range(n):
    if a[i] > 5:
        sum += a[i]
print(sum)

#7(1)
a = [1, 21, -13, -9, 4, 4, 0, -7, 78, -61, -45, 53]
odd = 1
even = 0
for i in range(len(a)):
    if a[i] % 2 != 0:
        odd = odd * a[i]
    else:
        even += a[i]
print('Sum of even elements: ', even)
print('Product of odd elements: ', odd)
#7(2)
a = [1, 21, -13, -9, 4, 4, 0, -7, 78, -61, -45, 53]
m = a.index(max(a))
n = a.index(min(a))
Max = max(a)
Min = min(a)
a[m] = Min
a[n] = Max
print(a)

#8(1)
a = [1, 21, -13, -9, 4, 4, 0, -7, 78, -61, -45, 53]
p = 1
s = 0
for i in range(len(a)):
    p = p*a[i]
    s += a[i]
print('Product of the array: ', p)
print('Sum of the array: ', s)

#9(1)
import math
n = int(input('Enter the length of array: '))
a = []
for i in range(n):
    print('Enter the element: ')
    a.append(int(input()))
print(math.fabs(min(a)))
a.reverse()
print(a)

#10(1)
a = []
n = 10
d = []
for i in range(n):
    a.append(int(input('Enter the array elements(10): ')))
for i in range(n):
    if a[i] == a[i-1]:
        d.append(a[i])

if len(d) == 0:
    print('There is no duplicate elements.')
else:
    print('Duplicate elements: ', d)

#10(2)
a = []
n = 15
for i in range(n):
    a.append(int(input('Enter the array elements(15): ')))
for i in range(15):
    if a[i] < 10:
        a[i] = 0
    if a[i] > 20:
        a[i] = 1

print(a)