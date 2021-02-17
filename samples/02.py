def hello_n(name: str,
            n: int):
    for i in range(n):
        print(name, "привет")


misha = "Миша", 4
hello_n("Вася", 5)
hello_n("Петя", 3)
hello_n(*misha)
