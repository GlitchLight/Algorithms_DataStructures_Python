# Даны целые числа n и m. Найти остаток от деления числа n на m.

def fib_mod(n, m):
    a=0
    b=1
    p=[0,1]
    T=1
    if n==1:
        return(1)
    i=2
    while 1>0:
        if (a+b) >= m:
            p.append((a+b)%m)
        else:
            p.append(a+b)
        a=b
        b=p[i]
        l=len(p)
        if (l%2==0)&(p[int(l/2)-1]==p[l-1]):
            if p[0:int(l/2)]==p[int(l/2):l]:
                T=int(l/2)
                break
        i+=1
    mod=p[n%T]
    return(mod)

def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
