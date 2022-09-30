#1(1)
A = []
N = int(input("Input matrix size: "))
for i in range(0, N):
    row = []
    for j in range(0, N):
        row.append(int(input("Input elements: ")))
    A.append(row)
sum = 0
for i in range(0, N):
    sum += A[i][i]
print(sum)

#1(2)       

 
def minelement(arr):
    no_of_rows = len(arr)
    no_of_column = len(arr[0])
    for i in range(no_of_rows):
        min1 = 0
        for j in range(no_of_column):
            if arr[i][j] < arr[0][0] :
                min1 = arr[i][j]
        print(min1)
arr = [[3, 4, 0, 8],
       [1, 4, 9, 11],
       [76, 34, 21, 1],
       [2, 1, 4, 5]]     
minelement(arr)

#2(1)
def isMagicSquare( mat) :
  n = len(mat)
  sumd1=0
  sumd2=0
  for i in range(n):
    sumd1+=mat[i][i]
    sumd2+=mat[i][n-i-1]
  if not(sumd1==sumd2):
    return False
  for i in range(n):
    sumr=0
    sumc=0
    for j in range(n):
      sumr+=mat[i][j]
      sumc+=mat[j][i]
    if not(sumr==sumc==sumd1):
      return False
  return True
mat = [ [ 2, 7, 6 ],
        [ 9, 5, 1 ],
        [ 4, 3, 8 ] ]
     
if (isMagicSquare(mat)) :
    print( "Magic Square")
else :
    print( "Not a magic Square")

#2(2)
def interchangeFirstLast(mat, n, m):
    rows = n
 
    # swapping of element between
    # first and last columns
    for i in range(n):
        t = mat[i][0]
        mat[i][0] = mat[i][n-1]
        mat[i][n-1] = t
 
 
# Driver code
   mat = [[8, 9, 7, 6],
          [4, 7, 6, 5],
          [3, 2, 1, 8],
          [9, 9, 7, 7]]
 
    n = 4
    m = 4
 
    interchangeFirstLast(mat, n, m)
    for i in range(n):
        for j in range(m):
            print(mat[i][j], end=" ")
        print("\n")

#3(1)
def transpose(mat, tr, N):
    for i in range(N):
        for j in range(N):
            tr[i][j] = mat[j][i]
  
def isSymmetric(mat, N):
     
    tr = [ [0 for j in range(len(mat[0])) ] for i in range(len(mat)) ]
    transpose(mat, tr, N)
    for i in range(N):
        for j in range(N):
            if (mat[i][j] != tr[i][j]):
                return False
    return True
  
mat = [ [ 1, 3, 5 ], [ 3, 2, 4 ], [ 5, 4, 1 ] ]
if (isSymmetric(mat, 3)):
    print "Yes"
else:
    print "No"

#3(2)
def search(mat, n, x):
    if(n == 0):
        return -1
    for i in range(n):
        for j in range(n):
            if(mat[i][j] == x):
                print("Element found at (", i, ",", j, ")")
                return 1
 
    print(" Element not found")
    return 0
 
mat = [[10, 20, 30, 40], [15, 25, 35, 45],
       [27, 29, 37, 48], [32, 33, 39, 50]] 
search(mat, 4, 29)

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