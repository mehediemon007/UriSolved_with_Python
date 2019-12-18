import sys
while True:
    text = input()
    if text == "":
        break
    else:
        numberOfBulb = int(input())
        bulnIndex = [int(i) for i in input().split()]
        # listOftext = list(text)

        message=[]
        for i in bulnIndex:
            # alphabet = listOftext[i-1]
            alphabet = text[i-1]
            message.append(alphabet)

        print("".join(message))
