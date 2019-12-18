import re
text = input()
text1 = re.split('[.-]',text)
for i in text1:
    print(i)

#uri 2950

input1 = list(map(int,input().split()))
res = input1[0]/(input1[1]+input1[2])
print("%.2f"%res)