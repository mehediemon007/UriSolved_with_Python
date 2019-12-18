x = int(input())

LedValue = [6,2,5,5,4,5,6,3,7,6]


while x > 0:
   sum = 0
   Value = list(map(int,input()))
   for i in Value:
        sum+=LedValue[i]
   print("%d leds"%sum)


   x-=1