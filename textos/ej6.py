"""Extraer subcadenas usando slicing (rebanado de cadenas sin usar listas)."""

cad = str(input("Dime una cadena de caracteres: "))

subCad = cad[:5]
print(subCad)

subCad = cad[5:]
print(subCad)

subCad = cad[::-1]
print(subCad)