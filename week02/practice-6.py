#1(1)
y = int(input("amount of elements: "))
x = [int(input("print element: ")) for i in range(y)]

g = 0
for i in range(y):
    if x[i] > g:
        g = x[i]
print("greatest number",str(g))
x.reverse()
print(x)

#1(2)
y = int(input("amount of elements: "))
x = [int(input("print element: ")) for i in range(y)]

g = 0
sum = 0
f=0
for i in range(y):
    sum += x[i]
    f+=1
for i in range(y):
    if x[i] == 0:
        x[i] = (sum/f)

print(x)

#2(1)
y = int(input("amount of elements: "))
x = [int(input("print element: ")) for i in range(y)]

x.sort()
print("lowest number",x[0])
print("index of lowest number - 0" )

#2(2)

x = [-1,2,-3,4]
y=[]
z=[]
for i in range (len(x)):
    if x[i] >=0:
        y.append(x[i])
    if x[i]<0:
        z.append(x[i])
print(x)
print(y)
print(z)

#3(1)

n = int(input("amount of elements: "))
t = [int(input("print element: ")) for i in range(n)]


sum = 0

for i in range(n):
    if t.index(t[i],0,len(t)) %2 == 0:
        sum += t[i]
        


print("summ of odd elements", str(sum))
print(t)
print("amount of elements",str(len(t)))

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

#11(1)
a = [26, 10, 0, -3, -15, 61, 74, 99, 12, 14, 51]
b = []
for i in range(len(a)):
    if a[i] % 2 == 0:
        b.append(a[i])
print(max(b))

#11(2)
a = [26, 10, 0, -3, -15, 61, 74, 99, 12, 14, 51]
b = []
for i in range(len(a)):
    if a[i] < 10 and a[i] % 2 == 0:
        b.append(a[i])
b.reverse()
if len(b) == 0:
    print('There is no such elements.')
else:
    print(b)

#12(1)
a = [26, 10, 0, -3, -15, 61, 74, -99, 12, 14, 51]
b = []
for i in range(len(a)):
    if a[i] < 10 and a[i] % 2 != 0:
        b.append(a[i])
print(min(b))




