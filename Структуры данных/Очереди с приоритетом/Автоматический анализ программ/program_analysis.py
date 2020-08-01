# Вход
# Первая строка содержит числа n,e,d. 
# Каждая из следующих e строк содержит два числа i и j и задаёт равенство xi = xj.
# Каждая из следующих d строк содержит два числа i и j и задаёт неравенство xi != xj. 
# Переменные индексируются с 1: x1,...,xn.

# Формат выхода. Выведите 1, если переменным x1,...,xn можно присвоить целые значения, чтобы все равенства и неравенства выполнились.В противном случае выведите 0

n,e,d=[int(i) for i in input().split()]
parent=[i for i in range(n)]

def root(index):
    while index!=parent[index]:
        index=parent[index]
    return(index)

for i in range(e):
    a,b=[int(i) for i in input().split()]
    index=root(a-1)
    if parent[b-1]!=index:
        parent[b-1]=parent[index]

state=1
for i in range(d):
    a,b=[int(i) for i in input().split()]
    index=root(a-1)
    if parent[b-1]==parent[index]:
        state=0
        break
print(state)