while True:
    s = input('Введите что-нибудь : ')
    if s == 'выход':
        break
    if len(s) < 3:
        print('В введённой строке '+s, 'всего', len(s), 'символа - это слишком мало')
        continue
    print('Введённая строка "'+s+'" достаточной длины -', len(s))
# Разные другие действия здесь...
print('Завершение')