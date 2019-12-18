values = list(map(int,input().split()))
Reindeer = ['Rudolph','Dasher', 'Dancer', 'Prancer', 'Vixen', 'Comet', 'Cupid', 'Donner', 'Blitzen']
sumV = sum(values)
indexV = sumV%9
print(Reindeer[indexV])