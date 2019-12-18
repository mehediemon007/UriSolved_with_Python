testcase = int(input())
hobbits=0
human=0
magician=0
dwatves=0
evel=0

while testcase > 0:
    Value = input().split(maxsplit=1)
    if Value[1] == 'X':
        hobbits+=1
    elif Value[1] == 'H':
        human+=1
    elif Value[1] == 'M':
        magician+=1
    elif Value[1] == 'A':
        dwatves+=1
    elif Value[1] == 'E':
        evel+=1

    testcase-=1

print("%d Hobbit(s)"%hobbits)
print("%d Humano(s)"%human)
print("%d Elfo(s)"%evel)
print("%d Anao(s)"%dwatves)
print("%d Mago(s)"%magician)
