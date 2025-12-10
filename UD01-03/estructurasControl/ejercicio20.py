"""Escriba un programa que lea una calificación numérica entre 0 y 10 y la transforme en la
calificación alfabética, escribiendo el siguiente resultado (switch).
• De 0 a < 3 Muy Deficiente.
• De 3 a < 5 Insuficiente.
• De 5 a < 6 Suficiente.
• De 6 a < 7 Bien.
• De 7 a <9 Notable.
• De 9 a 10 Sobresaliente
"""

nota = float(input("Dime cuanto has sacado:"))

if 0<nota<=3:
    print("Muy deficiente")
elif 3<nota<=5:
    print("Insuficiente")
elif 5<nota<=6:
    print("Suficiente")
elif 6<nota<=7:
    print("Bien")
elif 7<nota<=9:
    print("Notable")
elif 9<nota<=10:
    print("Sobresaliente")
else:
    print("No es una nota evaluable")