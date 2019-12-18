#from array import *

N = int(input())

while N > 0:
    name = input()
    degreeOfDive = float(input())
    marks = [float(i) for i in input().split()]

    maxValue = max(marks)
    minValue = min(marks)

    sumValue = sum(marks)-maxValue-minValue
    print("%s %.2f"%(name,sumValue*degreeOfDive))
    # print(name,"{0:.2f}".format(sumValue*degreeOfDive))
    #print(name+" "+ str(sumValue*degreeOfDive))
    N-=1