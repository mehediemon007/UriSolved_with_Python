totalList = [[int(i) for i in input().split()]for j in range(2)]
sum = 0
for i in range(3):
    if totalList[1][i] >= totalList[0][i]:
        sum+=totalList[1][i] - totalList[0][i]


print(sum)