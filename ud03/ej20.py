"""Dibuja un ordinograma de un programa que lea un número positivo N y calcule y visualice
su factura N! siendo el factorial:
0!=1
1!=1
2!=2*1
…
N!= N*(N-1)*(N-2)*…*1
"""

n = int(input("Dame un numero mayor que 0: "))
res = 1

if n>=0:
    for i in range(1,n+1):
        res = res*i
    print(res)
else:
    print("Error, el numero debe ser mayor a 0")