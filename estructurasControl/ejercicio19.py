"""Escriba un programa que simule un cajero automático con un saldo inicial de 1000 dólares,
con el siguiente menú de opciones:
Bienvenido a su Cajero Virtual
1. Ingresar dinero en cuenta
2. Retirar dinero de la cuenta
3. Salir
"""
opcion = 0
while opcion != 3:
    print("Bienvenido a su Cajero Virtual\n"
          "1. Ingresar dinero en cuenta\n"
          "2. Retirar dinero de la cuenta\n"
          "3. Salir\n")
    opcion = int(input("Dime el numero de la opcion que quieres realizar: "))
    
    match opcion:
        case 1:
            ing = float(input("Cuanto dinero desea ingresar?:"))
            print(f"Ha ingresado {ing}€")
        case 2:
            ret = int(input("Cuanto dinero desea sacar?: "))
            print(f"Ha sacado {ret}€")
        case 3:
            print("Que tenga un buen dia")
        case _:
            print("No se ha introducido una de las opciones")
            