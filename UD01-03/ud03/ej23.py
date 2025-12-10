"""Dibuja un ordinograma de un programa que lea una secuencia de números no nulos hasta
que se introduzca un 0, y luego muestre si ha leído algún número negativo, cuantos positivos y
cuantos negativos
"""


cont = 1
contPos = 0
contNeg = 0
negativo = False

while cont != 100:
    num = int(input("Inserta un numero positivo o negativo"))
    
    if num>0:
        print("Es positivo")
        cont = cont + 1
        contPos = contPos + 1
    else:
        print("Es negativo")
        cont = cont +1
        contNeg = contNeg + 1
        negativo= True
        
if not negativo:
    print("No hay negativos")
else:
    print(f"Hay negativos")
    
print(f"Hay {contPos} numeros positivos y {contPos} numeros negativos")