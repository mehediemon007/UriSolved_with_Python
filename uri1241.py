testCase = int(input())

while testCase > 0:
    numberA,numberB= [int(i) for i in input().split()]

    if numberA < numberB:
        print("nao encaixa")
    elif numberA == numberB:
        print("encaixa")

    else:
        while numberB!=0:

              if numberB%10 != numberA%10 :
                  print("nao encaixa")
                  break

              numberB //=10
              numberA //=10
        else:
            print("encaixa")


    testCase-=1