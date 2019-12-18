testcase = int(input())

while testcase > 0:
    Values = [int(i) for i in input().split()]
    qution = Values[0]//Values[1]
    reminder = Values[0]%Values[1]
    print(qution+reminder)
    testcase-=1

# uri 2863

testcase = int(input())
time =[]
while testcase > 0:
    time.append(float(input()))
    testcase-=1
print(min(time))