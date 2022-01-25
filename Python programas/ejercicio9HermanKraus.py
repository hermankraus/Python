def laboratorio(miligramos, temp, mayorMg, mayorCat, mayor):
    mg=0
    temperatura=0
    mayorCat=0
    mayorMg=0

    for i in range (1,27):
        print("Categoria numero: ", i)

        mg=float(input("Ingrese los miligramos a usar\n"))

        while mg<0:
            mg=float(input("Cantidad erronea. Ingrese nuevamente los miligramos a usar\n"))
        
        miligramos.append(mg)

        temperatura=int(input("Ingrese la temperatura de fusion\n"))

        temp.append(temperatura)

        if mayorMg<mg:
            mayorMg=mg
            mayorCat=i

        mayor.append(mayorMg)
        mayor.append(mayorCat)
    
        

###ALGORITMO PRINCIPAL

miligramos=[]
temp=[]
mayor=[]
mayorMg=0
mayorCat=0
total=0
contadorMg=0
contadorTemp=0
porcentaje=0
i=int
x=int

laboratorio(miligramos, temp, mayorMg, mayorCat, mayor)

for i in range (len(miligramos)):
    total=total+miligramos[i]

    if miligramos[i]>10 and miligramos[i]<20:
        contadorMg=contadorMg+1

for x in range (len(temp)):

    if temp[x]>50:
        contadorTemp=contadorTemp+1

porcentaje=contadorTemp/len(temp)*100


print("El peso total de los materiales reactivos es: ", total)
print("El total de reactivos que requieren entre 10 y 20 miligramos es: ", contadorMg)
print("La categoria ", mayor[1], " es la que mayor cantidad consume con un total de ", mayor[0]," miligramos.\n" )
print("El porcentaje de reactivos con temperatura superior a los 50 grados centigrados es : %", porcentaje)


            