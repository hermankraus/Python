horas=0
minutos=0
veinticinco=0
max=-999999999
min=9999999999
horaMax=0
horaMin=0
minMax=0
minMin=0
while horas!=24:
    if minutos==30:
        horas=horas+1
        minutos=0
    elif minutos==0:
        minutos=30

    temp=int(input("Ingrese la temperatura.\n"))

    if temp>25:
        veinticinco=veinticinco+1
    
    if max<temp:
        max=temp
        horaMax=horas
        minMax=minutos
    
    if min>temp:
        min=temp
        horaMin=horas
        minMin=minutos


print("La temperatura supero los 25 grados centigrados unas ", veinticinco, " veces.\n")
print("La temperatura maxima fue de ", max," a las ", horaMax," ", minMax, " minutos.\n")
print("La temperatura minima fue de ", min," a las ", horaMin," ", minMin, " minutos.\n")