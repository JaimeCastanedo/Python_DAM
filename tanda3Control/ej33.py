"""
Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un
dado de seis caras y muestre por pantalla el número en letras (dato cadena) de la cara opuesta
al resultado obtenido.

Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el
mensaje: "ERROR: número incorrecto."

"""

cara = int(input("Dime la cara que ha salido: "))

match cara:
    case 1:
        print("La cara opuesta es 6")
    case 2:
        print("La cara opuesta es 5")
    case 3:
        print("La cara opuesta es 4")
    case 4:
        print("La cara opuesta es 3")
    case 5:
        print("La cara opuesta es 2")
    case 6:
        print("La cara opuesta es 1")
    case _:
        print("No es un valor valido")