"""Verificar si un carácter específico está en la cadena con un ciclo y comparaciones."""

cad = str(input("Dime una cadena de caracteres: "))
char = str(input("Dime el caracter que deseas comprobar: "))
esta = False

for i in cad:
    if i == char:
        esta = True

if esta:
    print("El caracter está en la cadena")
else:
    print("El caracter no está en la cadena")