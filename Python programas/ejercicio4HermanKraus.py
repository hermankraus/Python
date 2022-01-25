sumaPiezas=int
piezas=int
seguir=int(input("Para comenzar presione 1.\n"))

while seguir<0 and seguir>1:
        print("Ingrese una opcion valida.\n")
        seguir=int(input("Ingrese 1 si desea ingresar datos de fabricacion.\n"))


while seguir==1:
    maquina=int(input("Ingrese el codigo de la maquina.\n"))

    while maquina<1:
        
        maquina=int(input("Codigo incorrecto, ingrese nuevamente el codigo a registrar.\n"))

    print("Ingrese el tiempo de trabajo semanal de la maquina.\n")
    horas=int(input("Ingrese las horas de trabajo:"))
    minutos=int(input("Ingrese los minutos de trabajo:"))
    while minutos>=60:
        minutos=int(input("Maximo permitido 60 minutos, ingrese nuevamente.\n"))
    segundos=int(input("Ingrese los segundos de trabajo:"))
    while segundos>=60:
        segundos=int(input("Maximo permitido 60 segundos, ingrese nuevamente.\n"))
    segundosTotales=int
    segundosTotales=segundos+minutos*60+horas*3600

    piezas=int(input("Ingrese la cantidad de piezas realizadas en el tiempo registrado.\n"))

    while piezas<0:
        
        piezas=int(input("Cantidad erronea, ingrese nuevamente una cantidad positiva de piezas.\n"))

    rendimiento=float
    rendimiento=piezas/segundosTotales

    print("El rendimiento de la maquina de codigo ", maquina," es: ",rendimiento)

    
    sumaPiezas=(int(sumaPiezas)+int(piezas))

    seguir=int(input("Ingrese 1 para ingresar los datos de la siguiente maquina, ingrese 0 para finalizar el programa.\n"))
    
    if seguir==0:
        print("Fin del programa.\n")
        break

print("El total de piezas fabricadas fue: ", int(sumaPiezas))
sumaPiezas=0

    