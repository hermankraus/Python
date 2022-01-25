def talladores(pesos, purezas, colores, colors):
    
    peso=float
    pureza=str
    color=str
   
    for x in range (1, 16):

        print("Ingrese la informacion del tallador: ", x)
        diamantes=int(input("Ingrese la cantidad de diamantes a ingresar."))

        while diamantes<0:
            print("Cantidad de diamantes invalida, ingrese nuevamente.\n")
            diamantes=int(input())

        for i in range (diamantes):

            peso=float(input("Ingrese el peso del diamante "+ str(i+1)+ "\n"))

            while peso<0:
                print("Peso invalido, ingrese nuevamente.\n")
                peso=float(input())

            pesos.append(peso)

            pureza=str(input("Ingrese la pureza del diamante.\n"))

            while len(pureza)!=3:
                print("La pureza debe ser de 3 letras.")
                pureza=str(input("Ingrese la pureza del diamante.\n"))

            purezas.append(pureza)

            color=str(input("Ingrese el color del diamante\n"))
            
            while color.lower() not in colores:
                print("El color debe estar entre la D y la Z.")
                color=str(input("Ingrese El color del diamante del diamante.\n"))

            colors.append(color)


### ALGORITMO PRINCIPAL

pesos=[]
purezas=[]
colors=[]
colores=['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
dg=['d', 'e', 'f', 'g']
contador_dg=0
suma=0
i=int
j=int
talladores(pesos, purezas, colores, colors)

for j in colors:
    if j.lower in dg:
        contador_dg+1

for i in range (len(pesos)):
    suma=(suma+pesos[i])

print("La cantidad de diamantes entre D y G son: ", contador_dg)
print("El pesos total de diamantes es : ", suma)
print("La cantidad de diamantes tallados es: ", len(colors))