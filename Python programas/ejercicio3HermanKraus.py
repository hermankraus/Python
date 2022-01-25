min=99999
diaMin=0
ventiladoresMin=0
turnoMin=str

max=0
diaMax=0
ventiladoresMax=0
turnoMax=str


seguir=int(input("Para comenzar presione 1.\n"))

while seguir<0 and seguir>1:
        print("Ingrese una opcion valida.\n")
        seguir=int(input("Ingrese 1 si desea ingresar datos de fabricacion.\n"))


while seguir==1:
    dia=int(input("Ingrese el dia del mes que desea registrar.\n"))

    while dia not in range(1,31):
        print("Ingrese un dia correcto.\n")
        dia=int(input("Ingrese el dia del mes que desea registrar.\n"))

    turno=str.upper(input("Ingrese el turno a registrar. M para mañana, T para tarde, N para noche.\n"))

    while turno!="M" and turno!="T" and turno!="N":

        print("Ingrese un turno correcto.\n")
        turno=str.upper(input("Ingrese el turno a registrar. M para mañana, T para tarde, N para noche.\n"))

    ventiladores=int(input("Ingrese la cantidad de ventiladores fabricados.\n"))

    while ventiladores<0:
        print("Ingrese una cantidad mayor o igual a 0.\n")     
        ventiladores=int(input("Ingrese la cantidad de ventiladores fabricados.\n"))

    if min>ventiladores:
        diaMin=dia
        turnoMin=turno
        ventiladoresMin=ventiladores

    if max<ventiladores:
        diaMax=dia
        turnoMax=turno
        ventiladoresMax=ventiladores

    seguir=int(input("Si desea continuar presione 1, para finalizar presione 0.\n"))

    while seguir<0 and seguir>1:
        seguir=int(input("Opcion invalida, ingrese nuevamente."))

    if seguir==0:
        print("Fin del programa.\n")
        break

    

print("El dia que menos ventiladores se fabricaron fue el dia ", diaMin," en el turno ", turnoMin, " con un total de ", ventiladoresMin, " ventiladores.\n")
print("El dia que mas ventiladores se fabricaron fue el dia ", diaMax," en el turno ", turnoMax, " con un total de ", ventiladoresMax, " ventiladores.\n") 

