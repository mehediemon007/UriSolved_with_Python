slides = list(map(int,input().split()))
#slides = [int(i) for i in input().split()]

A = slides[0]
B = slides[1]
C = slides[2]

if A + B > C and  B + C > A and C + A > B:
    if A==B and A==C:
        print("Valido-Equilatero")
    elif A!=B and B!=C and A!=C:
        print("Valido-Escaleno")
    elif A==C and B!=A  or B==C and A!=B or A==B and B!=C:
        print("Valido-Isoceles")

    if A*A == B*B + C*C or A*A + B*B == C*C or A*A + C*C == B*B:
        print("Retangulo: S")
    else:
        print("Retangulo: N")

else:
    print("Invalido")