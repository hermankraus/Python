x=int
dia=int
dia=0
maximo=0
codigoMax=0
totalHoras=0
empleados=[]
horas=[]
seguir=int(input("Ingrese 1 si desea comenzar el programa.\n"))

while seguir<0 and seguir>1:
        print("Ingrese una opcion valida.\n")
        seguir=int(input("Ingrese 1 si desea ingresar datos de empleados.\n"))

while seguir==1:
    for i in range(1,32):
        empleados=[]
        horas=[]
        siguiente=int(input("Para ingresar el dia laboral ingrese 1, para terminar ingrese 0.\n"))
        
        while siguiente<0 and siguiente>1 :
            print("Ingrese una opcion valida.\n")
            siguiente=int(input("Ingrese 1 si desea ingresar el dia laboral o 0 para terminar.\n"))

        print("DIA:",i)
        
        while siguiente==1:
            codigo=int(input("Ingrese el codigo del empleado.\n"))
            while codigo<0:
                codigo=int(input("Codigo invalido. Ingrese el codigo del empleado.\n"))

            while codigo in empleados:
                if codigo in empleados:
                    print("Este codigo ya existe.")

                codigo=int(input("Ingrese el codigo del empleado.\n"))
            
            if codigo not in empleados and codigo>0:
                empleados.append(codigo)


            hora=int(input("Ingrese las horas extras trabajadas."))
            while hora<0:
                hora=int(input("Hora invalida, ingrese nuevamente."))
            while hora in horas:
                if hora in horas:
                    print("Ya existe un empleado que trabajo esta cantidad de horas.")
                hora=int(input("Ingrese las horas extras nuevamente."))
    
            if hora not in horas and hora>0:
                horas.append(hora)
                totalHoras=totalHoras+hora
                if hora>maximo:
                    codigoMax=codigo
                    

            siguiente=int(input("Si desea ingresar mas empleados del mismo dia ingrese 1, para finalizar el dia ingrese 0.\n"))
        
        if siguiente==0:
            print("Fin del ingreso del dia.")
            dia=dia+1
            print("El empleado con mas horas extras trabajadas fue: ", codigoMax)
            print("El promedio de horas trabajadas fue: ", totalHoras/len(empleados))

    seguir=int(input("Desea seguir el programa? Ingrese 1 para seguir, 0 para salir.\n"))

if seguir==0:
    print("El total de dias trabajados fue: ", dia)
    print("Fin del programa.")

       
            
    