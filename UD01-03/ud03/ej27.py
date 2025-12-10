"""Dibuja un ordinograma de un programa que lea una secuencia de notas (con valores que
van de 0 a 10) que termina con el valor -1 y nos dice si hubo o no alguna nota con valor 10
"""

huboDiez = False

nota = float(input("Introduce una nota: "))

while nota != -1:
    if nota >= 0 and nota <= 10:
        if nota == 10:
            huboDiez = True
    else:
        print("Nota no válida. Debe estar entre 0 y 10.")
    
    nota = float(input("Introduce una nota: "))

if huboDiez:
    print("Sí hubo al menos una nota con valor 10.")
else:
    print("No hubo ninguna nota con valor 10.")