print("Ingrese un número del 1 al 7:")
opcion=input()
#opcion.isnumeric()
if(opcion.isnumeric()):
    opcion=float(opcion)
    if opcion==1:
        print("Es día LUNES")
    elif opcion==2:
        print("El día es MARTES")
    elif opcion==3:
        print("El día es MIÉRCOLES")
    elif opcion==4:
        print("El día es JUEVES")
    elif opcion==5:
        print("El día es VIERNES")
    elif opcion==6:
        print("El día es SÁBADO")
    elif opcion==7:
        print("El día es DOMINGO")
    else:
        print("El valor no es válido")
        print("Ingrese un número del 1 al 7")
        exit()
else:
    print("Ingrese un número para poder continuar")
    exit()