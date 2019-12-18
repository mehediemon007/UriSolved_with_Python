import array as ar
testcase = int(input())
GUni = 0
VGov = 0
while testcase > 0:
    Value = input().split(maxsplit=1)
    if Value[0] == 'V':
        VGov += int(Value[1])
    elif Value[0] == 'G':
        GUni += int(Value[1])

    testcase-=1

if (GUni-VGov) <=0:
    print("The strike will stop.")
else:
    print("NO CUT,FIGHT!")

# uri 2670
A1 = int(input())
A2 = int(input())
A3 = int(input())

time= []
time.append ((A2*2)+(A3*4))
time.append((A1+A3)*2)
time.append((A2*2)+(A1*4))

res = min(time)
print(res)


A1 = int(input())
A2 = int(input())
A3 = int(input())

if A2 >A1 and A2 >A3:
    print((A1+A3)*2)

elif A1 >A2 and A1>A3:
    print((A2*2)+(A3*4))

elif A3 >A1 and A3>A2:
    print((A1*4)+(A2*2))

elif (A1==A2 and A2>A3) or (A2==A3 and A2>A1) :
    print((A1 + A3) * 2)

elif A1==A3 and A1>A2:
    print((A2*2)+(A3*4))
elif A1==A2 and A2==A3:
    print((A1+A3)*2)

