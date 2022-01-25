'''
Ejercicio 1 – Socios Clubes

Luego de recabar datos de los socios en cada uno de los 17 clubes más importantes de la ciudad
se quiere determinar, para cada una de ellos, entre los censados mayores de edad (tienen 18 años o más)
quienes son más numerosos, los que son temporales (código 1) o los que son permanentes (código 2).
Para resolver esto se dispone, por cada socio de cada uno de los clubes, su código de asociado 
(1 para temporal, 2 para permanente) y la edad. Ver ejemplo.
Un código de asociado 0 (cero) indica que no hay más datos de ese club.
Valide el código entre 0, 1 y 2; no permita otros valores.
Validar la edad que no sea negativa y reconfirme si es mayor a 100.

'''

# Datos a ingresar codigo, edad
# for i in range(1,18):     para manejar los clubes
# while (codigo != 0):      while anidado dentro de for
# validar el codigo 0,1,2
# Chequear la edad la validez de la edad con un while para verificar no sea < 0 y > 100
# Reconfirme si es > 100
# Contadores para tipos de asociados


########   Programa Principal   #########



contador_uno=int
contador_dos=int

for i in range (0, 18):
    print ("Ingrese la cantidad de socios del club", i+1, "\n")
    socios=int(input())
    contador_dos=0
    contador_uno=0

    for i in range (socios) :
        
        print ("Ingrese el codigo del socio, 1 para permanentes, 2 para temporales y 0 para finalizar el ingreso por club.", i+1, "\n")
        codigo=int(input())
        if codigo==0:
                print("Fin de ingresos del club\n")
                break
        while codigo!=0:

            if codigo==1 or codigo==2:
                
                if codigo==1:
                    contador_uno=contador_uno+1
                else:
                    contador_dos=contador_dos+1

                edad = int(input("Escribe tu edad: "))

                while edad>100 and edad<0:

                    print("Edad incorrecta.")
                    edad = int(input("Escribe tu edad: "))

                if edad>100:
                        print("No se admiten socios mayores de 100 años. Ingrese su edad nuevamente.\n")
                        edad = int(input())
                    
            
                if (edad>0 and edad<18):
                    print("Usted es menor de edad.\n")
                    break
                elif edad>=18:
                    print("Usted es mayor de edad.\n")
                    break   
                        
        if codigo!=1 and codigo!=2 and codigo!=0:

            print("Codigo incorrecto, ingreselo nuevamente.\n")
            codigo=int(input())
            
    print("La cantidad de socios temporales son: ", contador_dos)
    print("La cantidad de socios permanentes son: ", contador_uno)

            
