"""Programa que muestre en líneas separadas lo siguiente:
ZYWXVUTSRQPONMLKJIHGFEDCBA, YWXVUTSRQPONMLKJIHGFEDCBA,
WXVUTSRQPONMLKJIHGFEDCBA, ...., DCBA, CBA, BA, A.
"""

cad = "ZYWXVUTSRQPONMLKJIHGFEDCBA"

for i in range(len(cad)):
    print(cad[i:])