"""

   ***   ***   ***   ***
   ***   ***   ***   ***
   ***   ***   ***   ***
***   ***   ***   ***   
***   ***   ***   ***   
***   ***   ***   ***   
   ***   ***   ***   ***
   ***   ***   ***   ***
   ***   ***   ***   ***
***   ***   ***   ***   
***   ***   ***   ***   
***   ***   ***   ***   

"""

a = int(input("Dime la altura de la figura, debe ser un numero par: "))

for i in range(a):
    if i % 2 == 0:
        for j in range(3):
            print("   ***" * a)
        
    else:
        for j in range(3):
            print("***   " * a)
