"""
*******
* *   *
*  *  *
*   * *
*  *  *
* *   *
*******
"""

a = int(input("Dime la altura de la figura, debe ser un numero impar: "))

for i in range(a):
    if i == 0 or i == a-1:
        print(a*"*")
    elif i < a//2:
        print("*" + " " * i + "*" + " " * (a-i-3) + "*")
    else:
        print("*" + " " * (a-i-1) + "*" + " " * (i-2) + "*")