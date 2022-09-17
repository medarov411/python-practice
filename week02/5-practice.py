#1
x = str(input("Enter the text: "))
print(x.split(' '))
y=0

if x[0]=='е':
    y+=1
for i in range(len(x)-1):
    if x[i] == ' ':
        if x[i+1]=='е':
            y+=1
    i+=1        
print(str(y), " - amount of words starting with 'e'") 

#2
x = str(input("Enter the text: "))
print(list(x))
y=0

for i in range(len(x)):
    if x[i] == ':':
        x.replace(":","%")       
        y+=1
      
print(str(y), " amount of replacement")

#3
x = str(input("Enter the text: "))
print(list(x))
y=0

for i in range(len(x)):
    if x[i] == '.':
        x.replace('.','')       
        y+=1
print(str(y), " amount of replacement")   

#4
x = str(input("Enter the text: "))
y=0
list(x)
for i in range(len(x)):
    if x[i] == "a":
        x.replace("a","o")       
        y+=1
print(str(y), " amount of replacement")
print(len(x.replace(' ', '')), " amount of characters")

#5
x = str(input("Enter the text: "))
print(x.upper())

#6
x = str(input("Enter the text: "))
y=0
list(x)
for i in range(len(x)):
    if x[i] == "a":
        x.replace("a","")       
        y+=1
print(str(y), " amount of removed")

#7
import math

x = str(input("Enter the text: "))
y=0
list(x)
for i in range(math.ceil(len(x)/2)):
    if x[i] == "n":
        x.replace("n","*")       
        y+=1
print(str(y), " amount of removed")

#8
x = str(input("Enter the text: "))
y=0
list(x)
for i in range(len(x)):
    if x[i] == " ":      
        y+=1
print(str(y+1), " amount of words")

#9
x = str(input("Enter the text: "))
n = str(input("Given word is: "))
y=0
x = x.split(" ")
 
for i in range(len(x)):
    if x[i]==n:
        y+=1
print(str(y), "amount of repeatings")        

#10
x = str(input("Enter the text: "))
x = list(x)
y=0

x[0] = "A"
for i in range(len(x)):
    if x[i] == " ":
        x[i+1]="A"
       
print(x)


#11 -

#12
f = str(input("Enter the text: "))
x = f.split(" ")
z = 0
y = list(f)


for i in range(len(y)):
    if y[i]==" ":
        if y[i-1]=="I":
            print(x[z])
            z+=1
if y[len(y)-1] == "I":
    print(x[len(x)-1])

