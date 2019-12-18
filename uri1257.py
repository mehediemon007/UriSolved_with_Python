testCase = int(input())

while testCase > 0:

    sum = 0
    line = int(input())
    i = 0
    while i < line:
        text = input()
        for j in range(len(text)):
            sum = sum+ord(text[j]) - 65 + i + j

        i+=1

    print(sum)
    testCase-=1
