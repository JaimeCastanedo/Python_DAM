"""Construir manualmente una nueva cadena añadiendo un carácter a la vez (ejemplo: filtrar caracteres o construir cadenas invertidas)."""

a = 1

while a != 0:
    cad = ""
    cad2 = str(input("Dime un caracter para crear una cadena, para terminar pulsa el numero 0: "))
    if a != 0:
        cad = cad + cad2
    else:
        a = 0

print(cad)