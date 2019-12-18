Salida=0
SalidaT=0
Vuelta=0
VueltaT=0
while True:
       report = input().split()
       if report[0] == 'ABEND':
           break
       elif report[0] == 'SALIDA':
            Salida+=1
            SalidaT+=int(report[1])

       elif report[0] == 'VUELTA':
            Vuelta+=1
            VueltaT+=int(report[1])


print(SalidaT-VueltaT)
print(Salida-Vuelta)