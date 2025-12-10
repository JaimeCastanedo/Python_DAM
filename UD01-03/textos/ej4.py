"""Construir manualmente una nueva cadena añadiendo un carácter a la vez (ejemplo: filtrar caracteres o construir cadenas invertidas)."""

nuevaCad = ""

cad = str(input("Dime una cadena de caracteres: "))

for i in cad:
    nuevaCad += i

print(nuevaCad)