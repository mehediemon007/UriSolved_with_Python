from array import *
x = int(input())


while x>0:
    text = list(map(str,input().split()))
    len1 = len(text[0])
    len2 = len(text[1])
    if len1>=len2:
         Len=len1
    else:
       Len = len2
    for i in range(Len):
        if i < len1:
            print(text[0][i],end="")
        if i < len2:
            print(text[1][i],end="")

    print("")
    x-=1
