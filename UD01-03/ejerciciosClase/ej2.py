"""
Estrella 8 puntas
*   *   *
 *  *  *
  * * *
*********
  * * *
 *  *  *
*   *   *
"""

a = int(input("Dime la altura de la figura, debe ser un numero impar: "))


for i in range(a):
    for j in range(a):
        if i == a // 2:
            print("*", end="")
        elif j == i or j == a // 2:
            print("*", end="")
        elif j == a - 1 - i:
            print("*", end="")
        else:
            print(" ", end="")
    print() 