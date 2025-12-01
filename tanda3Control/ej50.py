"""
Una persona se encuentra en el kilómetro 70 de una carretera, otra se encuentra en el km
150, los coches tienen sentido opuesto y tienen la misma velocidad. Realizar un programa para
determinar en qué kilómetro de esa carretera se encontrarán
"""
inicio = 70
fin = 150

while inicio != fin:
    inicio += 1
    fin -= 1

print(f"El kilometro en el que se encontraran es el {inicio}")