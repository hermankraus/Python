

def atletas(num_atletas):
    seguir=0
    atleta=int
    for x in range (1, 51):
        atleta=int(input("Ingrese el numero del atleta.\n"))

        while atleta<0:
            print("Codigo invalido, ingrese nuevamente.\n")
            atleta=int(input())

        num_atletas.append(atleta)

        seguir=int(input("Desea ingresar otro atleta? \n 1)SI.\n 2)NO.\n"))

        while seguir<1 or seguir>2:
            print("Codigo invalido, ingrese nuevamente.\n")
            seguir=int(input())

        if seguir==2:
            break


def saltos(salto1,salto2,salto3,descalificado,mayor_salto,ganador,num_atletas):
    mayor_salto=0
    for i in range (len(num_atletas)):
        print("Ingrese los saltos del atleta ", i+1)
        primero=int(input("Ingrese primer salto.\n"))

        while primero<0:
            print("Valor de salto invalido, ingrese nuevamente.\n")
            primero=int(input())

        salto1.append(primero)

        segundo=int(input("Ingrese segundo salto.\n"))

        while segundo<0:
            print("Valor de salto invalido, ingrese nuevamente.\n")
            segundo=int(input())
        
        salto2.append(segundo)

        tercero=int(input("Ingrese tercer salto.\n"))

        while tercero<0:
            print("Valor de salto invalido, ingrese nuevamente.\n")
            tercero=int(input())

        salto3.append(tercero)

        if salto1[i]>0 and salto2[i]>0 and salto3[i]>0:

            if mayor_salto<salto1[i]:
                mayor_salto=salto1[i]

            elif mayor_salto<salto2[i]:
                mayor_salto=salto2[i]

            elif mayor_salto<salto3[i]:
                mayor_salto=salto3[i]

            ganador=i
        elif primero==0 or segundo==0 or tercero==0:
            descalificado.append(i)

    print("El salto ganador fue: ", mayor_salto)
    print("El ganador es: ", num_atletas[ganador])
    return (ganador)



### ALGORITMO PRINCIPAL
   
num_atletas=[]
salto1=[]
salto2=[]
salto3=[]
descalificado=[]
mayor_salto=0
ganador=0


atletas(num_atletas)
saltos(salto1,salto2,salto3,descalificado,mayor_salto,ganador,num_atletas)

print("La cantidad de participantes son: ", len(num_atletas))

