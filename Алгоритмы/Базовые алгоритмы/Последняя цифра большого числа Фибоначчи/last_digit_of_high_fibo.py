# Дано число 1 ≤ n ≤ 10**7, необходимо найти последнюю цифру n n-го числа Фибоначчи.

def fib_digit(n):
    a=0
    b=1
    if n==1:
        return(1)
    else:
        for i in range(2,n+1):
            F=a+b
            a=b
            if F>9:
                F=F%10
            b=F
        return(F)


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()