"""Leer una cadena desde teclado y mostrarla carácter por carácter usando un ciclo for y el índice."""

cad = str(input("Dime algo: "))

for i in range (len(cad)):
    print(cad[i])


for i in cad:
    print(i)