text = input()

if text == "nenhuma":
    print("portugues")
elif text == "esquerda":
    print("ingles")
elif text == "direita":
    print("frances")
elif text == "as duas":
    print("caiu")

# uri 2826..........

Value = []
for i in range(2):
    Value.append(input())

Value.sort()
for i in Value:
    print(i)

#uri 1581

testcase = int(input())
while testcase > 0:
    GrpMem = int(input())
    tag=1
    language = []
    while GrpMem > 0:
        language.append(input())
        if language[0] != language[-1]:
            tag=0
        GrpMem-=1
    if tag == 1:
         print(language[0])
    else:
        print("ingles")

    testcase-=1