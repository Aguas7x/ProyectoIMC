# Programa que debe contener entre 4 y 8 letras para que sea correcto.
contador = 0 
while contador < 4: #Un bucle de ciclo while que nos dice que el contador debe ser menor que 4 para poder ejecutarlo ciclicamente hasta que
    #la palabra se correcta
    palabra1 = input("Introduce la primera palabra: ")
    if len(palabra1) >= 4 and len(palabra1) <= 8: #Si la palabra introducida por el usuario es correcta acaba el programa con break si no continua con elif
        print("La palabra es correcta")
        contador == 4  # y manda el contador a 4 para que no se repita el ciclo 
        break
    elif len(palabra1) < 4: #si no es correcta va sumando para al contador y nos dice cuantas letras faltan hacia hasta que se introduzca una palabra
        #con una longitud de entre 4 y 8 letras. y le sumara al contador 1 
        print('Hacen falta letras solo tienes', len(palabra1), 'letras.')
        contador = 1 + contador
    elif len(palabra1) > 8:
        print('Sobran letras,. tienes', len(palabra1), 'letras.')
        contador = 1 + contador
#al final si como nuestro contador debe ser menor a 4 para que se vuelva a ejecutar el codigo hasta qeu sea correcto basicamente tenemos 4 intentos


