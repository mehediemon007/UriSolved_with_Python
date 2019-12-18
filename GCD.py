import math
print("Enter two Value:")
x, y = int(input()), int(input())
i=1
gcd=0
while i<=x and i<=y:
    if x%i==0 and y%i==0:
        gcd=i
    i+=1

print(gcd)

if y > x:
    x,y = y,x

while y > 0:
    r = x%y
    x = y
    y=r

print(x)

print(math.gcd(x,y))

