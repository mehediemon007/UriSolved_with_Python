from numpy import *
array = array([1,2, 4],int)

R = int(input("Enter Number Of Rows:"))
C = int(input("Enter Number Of Columns:"))
matrix=[]
print("Enter Values:")
for i in range(R):
      a=[]
      for j in range(C):
          a.append(int(input()))
      matrix.append(a)

print("Print Values:")

for i in range(R):
      for j in range(C):
          print(matrix[i][j],end=" ")
      print()

# If we take input in one line.....
print("Take input in one line:")

print("Enter Values:")
for i in range(R):
      a=[]
      a.append([int(j) in input().split()])
      matrix.append(a)

print("Print Values:")

for i in range(R):
      for j in range(C):
          print(matrix[i][j],end=" ")
      print()

#Another way to take unput in one line

print("Enter Values:")
for i in range(R):
      a=[]
      a.append(list(map(int,input().split())))
      matrix.append(a)

print("Print Values:")
print(matrix)

#Another way to take input in one line and then use numpy array.rehape function

#another way
print("one-linear logic to take input:")
matrix = [[int(input()) for x in range (C)] for y in range(R)]

print("Print Values:")

for i in range(R):
      for j in range(C):
          print(matrix[i][j],end=" ")
      print()

matrix = [[int(j) for j in input().split()] for y in range(R)]

print("Print Values:")

for i in range(R):
      for j in range(C):
          print(matrix[i][j],end=" ")
      print()





