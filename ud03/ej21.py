"""Dibuja un ordinograma de un programa que lea 100 números no nulos y luego muestre un
mensaje de si ha leído número negativo o no.
"""

cont = 1
negativo = False

while cont != 100:
    num = int(input("Inserta un numero positivo o negativo (0 para salir)"))
    
    if num>0:
        print("Es positivo")
        cont = cont + 1
    else:
        print("Es negativo")
        cont = cont +1
        negativo= True
            
if not negativo:
    print("No hay negativos")
else:
    print(f"Hay negativos")