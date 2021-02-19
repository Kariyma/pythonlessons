a = []

for i in range(int(input('Количество элементов в списке '))):
    a.append(input(str(i) + ': '))

print(*a)
