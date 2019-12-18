ruensAndDefeatValue = list(map(int,input().split()))
sum=0
dicofruensValue = {}

while ruensAndDefeatValue[0] > 0:
    ruensValue = input().split()
    dicofruensValue[ruensValue[0]] = ruensValue[1]
    ruensAndDefeatValue[0]-=1

numOfrecit = int(input())
ValoeOfrecit = [str(i) for i in input().split()]

for i in ValoeOfrecit:
    sum+=int(dicofruensValue[i])

if sum>=ruensAndDefeatValue[1]:
    print(sum)
    print("You shall pass!")
else:
    print(sum)
    print("My precioooous")

