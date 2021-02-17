x = 0
print('1: x равно', x)


def func_outer():
    x = 2
    print('2: x равно', x)

    def func_inner():
        nonlocal x
        x = 5
    func_inner()
    print('Локальное x сменилось на', x)


func_outer()
print('3: x равно', x)
