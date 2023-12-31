'''Подвиг 5. Определите функцию-генератор, которая бы возвращала простые числа. 
(Простое число - это натуральное число, которое делится только на себя и на 1). 
Выведите с помощью этой функции первые 20 простых чисел c помощью оператора yield (начиная с 2) в одну строчку 
через пробел.'''

from sympy import isprime


# ! алгоритм быстр лишь на маленьких числах
def is_prime() -> int:
    i = 2
    while True:
        if isprime(i):
            yield i
        i += 1


gen = is_prime()
print(*(next(gen) for _ in range(20)))
