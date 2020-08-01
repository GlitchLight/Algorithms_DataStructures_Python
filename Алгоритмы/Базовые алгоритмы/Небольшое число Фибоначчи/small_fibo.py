# Дано целое число 1 <= n <= 40. Вычислить n-e число Фибоначчи

def fib(n):
    # put your code here
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(2, n + 1):
            F = a + b
            a = b
            b = F
        return F

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()