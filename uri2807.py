from numpy import *
t1 = 0
t2 =1
nextTerm =0

n = int(input())
val = []

for i in range(n):
    val.append(t2)
    nextTerm = t1 + t2
    t1 = t2
    t2 = nextTerm

# print list in reverse order not sort
val.reverse()
print(val)


#another way
print(val[::-1])

#another way.
for i in reversed(val[1:n]):
    print(i,end=" ")
print(val[0])
