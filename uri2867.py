testcase = int(input())

while testcase > 0:
    digit=0
    Value = list(map(int, input().split()))
    TotalVal = pow(Value[0],Value[1])
    while TotalVal != 0 :
        TotalVal//=10
        digit+=1
    print(digit)
    testcase-=1
