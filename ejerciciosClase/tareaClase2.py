"""
4
44
4 4
4  4
4   4
4444
"""

altura = int(input("Introduce la altura: "))

for i in range(altura):
    if i == 0:
        print('4')
    elif i == altura - 1:
        print('4' * altura)
    else:
        print('4' + ' ' * (i - 1) + '4')