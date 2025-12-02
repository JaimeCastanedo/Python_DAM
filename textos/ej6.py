"""Extraer subcadenas usando slicing (rebanado de cadenas sin usar listas)."""

cad = str(input("Dime una cadena de caracteres: "))
subCad = ""

for i in cad:
    subCad += cad[2,5]