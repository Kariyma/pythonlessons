while True:
    x = int(input())
    if x == 0:
        break
    y = int(input())
    if y == 0:
        break
    if x > 0 and y > 0:
        print(1)
    elif x < 0 < y:
        print(2)
    elif x < 0 and y < 0:
        print(3)
    elif x > 0 > y:
        print(4)
    else:
        print('НИКОГДА')
print('Завершено')
