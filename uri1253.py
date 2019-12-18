x = int(input())

while x > 0:
    text = list(input())
    ValforShift = int(input())

    for i in range(len(text)):
        if ord(text[i])-ValforShift < 65:
            text[i] = chr(91+(ord(text[i])-65)-ValforShift)
        else:
            text[i] = chr(ord(text[i])-ValforShift)

    for i in text:
        print(i,end="")
    print("")

    x-=1