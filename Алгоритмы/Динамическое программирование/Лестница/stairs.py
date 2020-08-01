# Даны число 1 <= n <= 10**2. ступенек лестницы и целые числа -10**4 <= a1, ..., an <= 10**4, которыми помечены ступеньки. 
# Найдите максимальную сумму, которую можно получить, идя по лестнице снизу вверх (от нулевой до nn-й ступеньки), каждый раз поднимаясь на одну или две ступеньки.

import sys
sys.setrecursionlimit(20000)

n = int(input())
cost_lst = [int(i) for i in input().split()]
cost_lst.insert(0,0)
i = 0
d={}
if n>0:
    d[0] = 0
    d[1] = cost_lst[1]

def F(index):
    if index in d:
        return(d[index])
    else:
        d[index] = max(F(index - 2) + cost_lst[index - 1] + cost_lst[index], F(index - 2) + cost_lst[index], F(index-1) + cost_lst[index])
        return d[index]

print(F(n))