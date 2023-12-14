'''# V.1
n = int(input('Введите размерность треугольника Паскаля: '))
P = []

for i in range(n):
    row = [1] * (i + 1)
    for j in range(i + 1):
        row[j] = P[i - 1][j - 1] + P[i - 1][j] if j != 0 and j != i else 1
    P += [row]
for el in P:
    print(el)'''

# V.2
from math import factorial as f


def pascal(n, m):
    return int(f(n) / (f(m) * (f(n - m))))


n = int(input('Введите размерность треугольника Паскаля: '))

print([pascal(n, i) for i in range(n + 1)])
