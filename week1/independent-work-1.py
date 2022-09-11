#Practice work 2
#1
import math
a=int(input("Enter first value: ")) 
b=int(input("Enter second value: "))
h=int(input("Enter third value: "))

s = (((a**2 + b)*h) / (2*(a-b)+4))

print("s={0:.2f}".format(s))

#Practice work2
#2
import math
x=int(input("Enter first value: ")) 
y=int(input("Enter second value: "))

h = (math.sqrt( math.cos(2*y) + math.sin(4*y) + math.sqrt(math.e**x + math.e**(-x))) / ( ((math.e**-x + math.e**x)**3) + (math.sin(4*y) + math.cos(2*y) -2)**2  )   )

print("H={0:.2f}".format(h))

#Practice work2
#3(1)
import math
x=2
y=1

result = (((x**y)**x) + ((x**x)**y) - x**4)
print("result={0:.2f}".format(result))

#Practice work2
#3(2)
import math
x=1
y=4
z=3
result = ( (math.fabs((1 / math.tan(x))+6))**(1/3) + math.sqrt(((x+1)**3) / (4*y - 2*z)))
print("result={0:.2f}".format(result))

#Practice work2
#3(3)
import math
x=3
y=0.2

result = ( ((5*x*y)/((x**3) -4)) + math.exp(x**2) + math.sqrt( (math.cos(y))**2 - y**2 ))
print("result={0:.2f}".format(result))


#Practice work2
#3(4)
import math
x=3
y=5

result = ( math.sqrt(math.fabs(y)) + ((math.atan(math.log(x))**3) / ( (x*y)-y+1) ))
print("result={0:.2f}".format(result))


#Practice work2
#3(1.2)
import math
x=3
y=1
z=2
result = ( (4**(x*y)) - (x**(y*z)) + (x*y)*z )
print("result={0:.2f}".format(result))

#Practice work2
#3(2.2)
import math
x=3
y=1
z=2
result = ((4*math.fabs(x) - x*y*z)/( x + (math.fabs(x*y)) - 2*y*z))
print("result={0:.2f}".format(result))

#Practice work2
#3(3.2)
import math
x=0.8
y=0.1
z=4
result = (   math.sqrt(1 - x + (math.pi/2 - math.atan(x-7*y)) / (4*x*z - math.log(y)**2)  )                     )
print("result={0:.2f}".format(result))

#Practice work2
#3(4.2)
import math
x=3
y=1
z=3
result = ( (  (2*3*4) ) /  ((math.sin(x)**3) + math.tan(y)**3)  )     
print("result={0:.2f}".format(result))

#Practice work2
#3(1.3)
import math
x=4

result = ( ((math.log(x-3)**4) +(2*x) * math.sin(3*x)**2)/((4*x) - 5.2 )  )     
print("result={0:.2f}".format(result))

#Practice work2
#3(2.3)
import math
x=2
y=2
z=1

result = ( math.sqrt(0.6*x*y*z) + ((y**x)**2) -math.exp(math.sin(2*x)) )     
print("result={0:.2f}".format(result))

#Practice work2
#3(3.3)
import math

x=0.5
y=2


result = ((math.asin(x**3) - 6) / (8*(math.cos(4*y)-math.sin(4*x))))     
print("result={0:.2f}".format(result))

#Practice work2
#3(4.3)
import math

x=2
y=1
z=3


result = (((math.fabs(math.log(x**3)) + math.exp(2*x)) / (x+3.4)) - ((math.cos(x)/math.sin(x))**3)*(3/(x*y*z)))     
print("result={0:.2f}".format(result))

#Practice work2
#area and p
import math

x = int(input("leg first: "))
y = int(input("leg second: "))


hypotenuse = math.sqrt((x**2) + (y**2))
area = (x*y)/2

p = x + y + hypotenuse

print("area: " + str(area))
print("perimeter: " + str(p))

#Practice work2
#roots
import math

a = float(input("first: "))
b = float(input("second: "))
c = float(input("third: "))



d = (b**2) - 4*a*c

if d>0:
    x1 = (-b + math.sqrt(d))/(2*a)
    x2 = (-b - math.sqrt(d))/(2*a)
    print("x1: " + str(x1))
    print("x2: " + str(x2))

elif d==0:
    x1 = -b/(2*a)
    print("x1: " + str(x1))

else:
    print("No roots, D<0")

#Practice work2
#Rectangles
print ( "1-rectangle, 2-triangle, 3-circle" ) 
figure = input ( "Select a shape:" )

if figure == '1' : 
    print ( "The lengths of the sides of the rectangle:" ) 
    a = float (input ( "a =" )) 
    b = float (input ( "b =" )) 
    print ( "Area:% .2f" % (a * b)) 
elif figure == '2' : 
    print ( "The lengths of the sides of the triangle:" ) 
    a = float (input ( "a =" )) 
    b = float (input ( "b =" )) 
    c = float (input ( "c =")) 
    p = (a + b + c) / 2 
    from math import sqrt 
    s = sqrt (p * (p - a) * (p - b) * (p - c))
    print ( "Area:% .2f" % s) 
elif figure == '3' : 
    r = float (input ( "Circle radius R =" )) 
    from math import pi 
    print ( "Area:% .2f" % (pi * r ** 2 )) 
else : 
    print ( "Input error" )

    



