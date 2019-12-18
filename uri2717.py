timeRemain = int(input())
A,B = list(int(j) for j in input().split())
sum = A + B
if sum <= timeRemain:
    print("Farei hoje!")
else:
    print("Deixa para amanha!")
