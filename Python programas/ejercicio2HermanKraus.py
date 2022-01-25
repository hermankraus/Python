'''
Ejercicio 2 – Central telefónica

Una central telefónica registra la duración de cada llamada, expresada en segundos.
A partir de esta información se quiere convertir la duración de cada llamada a:
horas, minutos y segundos y mostrarla.

Luego, al finalizar el ingreso de datos y el proceso de conversión, determinar:

    La cantidad de llamadas que superaron los 10 minutos.
    El promedio de duración de las llamadas (en segundos).
    La mínima duración de llamada (en segundos).

    No se sabe cuántas llamadas se han registrado, proponer un fin de datos.

''' 

# Datos: duración llamada en segundos.
# Estructura de contro: while.
# Convetir a horas, minutos y segundos
# Contar llamadas.
# Sumar --> luego hacer el promedio.
# Buscar el minimo.
# Mostrar resultados.

###########  Programa principal  ###########

contador=int(0)
suma=float(0)
minimo=int(99999999999999999999)
contador10=int(0)


seguir=int(input("Ingrese 1 si desea ingresar una llamada.\n"))
 
while seguir!=1:
        print("Ingrese una opcion valida.\n")
        seguir=int(input("Ingrese 1 si desea ingresar una llamada.\n"))


while seguir==1 :
    if seguir==1:
        contador=contador+1

    llamada=int(input("Ingrese duracion de llamada en segundos.\n"))
    
    suma=suma+llamada

    if llamada<minimo:
        minimo=llamada
    
    if llamada>600:
        contador10=contador10+1

    hora=int(llamada// 60// 60)
    minutos=int(llamada//60 % 60)
    segundos=int(llamada%60)

    print("Tiempo: {}:{}:{}".format(hora, minutos, segundos))

    seguir=int(input("Ingrese 1 si desea ingresar otra llamada, 0 para finalizar.\n")) 
    
    while seguir!=1 and seguir!=0:
        print("Ingrese una opcion valida.\n")
        seguir=int(input("Ingrese 1 si desea ingresar otra llamada, 0 para finalizar.\n"))

    if seguir==0:

        print("Fin del ingreso de llamadas.\n")
        break

print("La llamada que menos duro fue de ", minimo, " segundos\n")
minimo=0

print("El promedio de las llamadas en segundos es: ", suma/contador)
print("La cantidad de llamadas que superaron los 10 minutos son: ", contador10)
suma=0
contador=0
contador10=0