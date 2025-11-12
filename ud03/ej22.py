"""Dibuja un ordinograma de un programa que lea 100 números no nulos y luego muestre un
mensaje indicando cuántos son positivos y cuantos negativos
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
            
print(f"Hay {contPos} numeros positivos y {contPos} numeros negativos")