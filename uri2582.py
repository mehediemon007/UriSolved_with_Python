songList =['PROXYCITY','P.Y.N.G.','DNSUEY!','SERVERS','HOST!','CRIPTONIZE','OFFLINE DAY','SALT','ANSWER!','RAR?' ,'WIFI ANTENNAS']

textCase = int(input())
while textCase > 0:
    firstBTN,secondBTN = list(map(int,input().split()))
    print(songList[firstBTN+secondBTN])

    textCase-=1