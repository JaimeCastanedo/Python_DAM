"""Contar cuántas veces aparece un carácter dado en una cadena usando for y un contador."""

cad = str(input("Dime algo: "))
car = str(input("Dime una letra de tu frase: "))
cont = 0

for i in cad:
    if i == car:
        cont +=1

print(f"El caracter {car} aparece {cont} veces en la cadena: {cad}")
        