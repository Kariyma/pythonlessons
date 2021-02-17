def fool(x):
    print("10: это 'x' внутри функции", x)
    x[0] = 7
    print("11: это 'x' внутри функции", x)
    x = [4, 5, 6]
    print("12: это 'x' внутри функции", x)


def fun(x: str, y: int) -> str:
    result = x
    for i in range(y - 1):
        result += x
    return result


print(fun(2, 5))
print(fun('ма', 2))