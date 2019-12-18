def calculateC(list):
    switcher = {
        "suco de laranja":120,
        "morango fresco": 85,
        "mamao":85,
        "goiaba vermelha": 70,
        "manga":56,
        "laranja":50,
        "brocolis":34
    }
    #print(type(switcher.get(list[1],"no")))
    return switcher.get(list[1],"No value")*int(list[0])
    # print(switcher.get(list[1],"No value"))


while True:
    T = int(input())
    totalAmount = 0

    if T == 0:
        break

    else:
        while T !=0:
            #listofFood = list(map(str,input().split()))
            #listofFood = input().split(maxsplit=1)
            listofFood=[]
            # a,b = int(input()), input()
            a,b = input().split(maxsplit=1)
            listofFood.append(a)
            listofFood.append(b)
            totalAmount += calculateC(listofFood)
            # calculateC(listofFood)
            T-=1

        if totalAmount > 130:
            print("Menos %d mg"%(totalAmount-130))
        elif totalAmount < 110:
            print("Mais %d mg"%(110-totalAmount))
        else:
            print("%d mg"%totalAmount)