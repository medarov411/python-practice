#1
price = int(input("The price of 1kg sweets: "))
n = 10
x=0

for i in range(n):
    i+=1
    x+=price
    print("Price of ",str(i),"kg =",str(x))


#2
x=0
total=0
lst = []

for i in range(0, 100):
    ele = int(input("Enter the number: "))
    if ele==0:
        break
    lst.append(ele)
      
while (x<len(lst)):
    total+=lst[x]
    x+=1
print("Sum of all elements: ", total)
print("Number of elements in sequence: ", len(lst))
 
