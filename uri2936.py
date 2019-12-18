portionValue = [300,1500,600,1000,150]
i = 0
total = 0
while i < 5:
    perPortion = int(input())
    total += (portionValue[i]*perPortion)
    i += 1
print(total+225)

# uri 2987

Alphabet = input()

print(ord(Alphabet)-64)
