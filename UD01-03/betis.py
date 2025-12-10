"""
****************
 *   *   *   *
   * *   * *
     *   *
       *
"""

a = int(input("Dime la altura: "))

for i in range(a):
    if i == 0:
        print("*"*((a*3)+(a//2)))
    elif i == a-1:
        print(" "*(2*a-3) + "*")
    else:
        print(" "*(i*2-1) + "*" + " " * (4*(a-i)-5) + "*")
