"""
Figura:

*************
* * * * * * *
*************
* * * * * * *
*************
* * * * * * *
*************
"""

a = int(input("Dime la altura de la figura: "))

for i in range(a):
    if i % 2 == 0:
        print("*"*((a*2)-1))
    else:
        print(("*" + " ") * (a-1) + "*")