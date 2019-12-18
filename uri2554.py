while True:
    NF , ND = list(map(str,input().split()))
    if NF == "" and ND=="":
        break
    else:
        FV = 1
        for i in range(int(ND)):
                Tag=0
                EachValue = [str(i) for i in input().split()]
                for i in range(1,len(EachValue)):
                        if i == '0':
                            break
                else:
                   Tag=1