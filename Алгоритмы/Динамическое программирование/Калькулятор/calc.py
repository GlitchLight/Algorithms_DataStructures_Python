# У вас есть примитивный калькулятор, который умеет выполнять всего три операции с текущим числом x: заменить x на 2x, 3x или x+1. По данному целому числу 1 <= n <= 10**5.
# определите минимальное число операций k, необходимое, чтобы получить nn из 1. Выведите kk и последовательность промежуточных чисел.

n = int(input())
D = [0] + [1000 for i in range(n-1)]
previouses = [0 for i in range(n)]
answer = [n, ]

for i in range(1, n+1):
    for k in (i*2, i*3, i+1):
        if (k-1) < n and D[i-1] + 1 < D[k-1]:
            D[k-1] = D[i-1] + 1
            previouses[k-1] = i

while n > 1:
    answer.append(previouses[n-1])
    n = previouses[n-1]

print(D[-1])
print(*list(reversed(answer)))
