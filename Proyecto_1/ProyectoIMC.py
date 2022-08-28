#Cantidad de peresonas que haran el calculo de su IMC
personas = int(input( "personas: "))
#Ciclo while para poder repetir las instrucciones en el caso de que haya mas de 1 persona
while personas > 0:
#Campo de solicitud de nombre, apellidos, edad, peso y estatura
    nombre = input('Nombre: ')
    apellido = input('Apellido paterno: ')
    apellido_materno = input('Apellido materno: ')
    edad = int(input('Introduce tu edad en años: '))
    peso = float(input('Introduce tu peso en kg: '))
    estatura = float(input('Introduce tu estatura en metros: '))
#calculo de indice de masa corporal
    IMC = peso / estatura**2
#Impresion de IMC
    print('Buen dia ' +   nombre + ' ' + apellido + ' ' + apellido_materno)
    print("Su IMC es: " + str(IMC))
#Validaciones de peso
    if IMC >= 0 and IMC <= 18.90:
        print ("Delgadez leve")
    elif IMC >= 18.50 and IMC <= 24.99 :
        print ("Normal")
    elif IMC >= 25.00 and IMC <= 29.99:
        print ("Sobrepeso")
    elif IMC >= 30.00 and IMC <= 34.99:
        print ("obesidad leve")
    elif IMC >= 35.00 and IMC <= 39.00:
        print ("obesidad media")
    elif IMC >= 40.00:
        print ("obesidad morbida")
#Condicion para detener el ciclo
    personas = personas - 1