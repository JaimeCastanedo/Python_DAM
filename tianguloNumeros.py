a = int(input("Dime la altura: "))

for i in range(a+1):
    print(" "*(a-i) + (str(i) + " ")*i)