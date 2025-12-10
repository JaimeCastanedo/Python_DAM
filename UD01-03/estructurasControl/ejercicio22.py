"""Escriba un programa que recibe como datos de entrada una hora expresada en horas,
minutos y segundos que nos calcula y escribe la hora, minutos y segundos que serán,
transcurrido un segundo.
"""

hora = int(input("Dime la hora: "))
min = int(input("Dime los minutos: "))
seg = int(input("Dime los segundos: "))

seg = seg + 1

if seg > 59:
    min = min + 1
    seg = 00
if min > 59:
    hora = hora + 1
    min = 00
if hora > 23:
    hora = 00
    
print(f"La hora mas un segundo es: {hora}:{min}:{seg}")