# В первой строке даны целое число 1 <= n <= 10**5. и массив A[1 ... n] из n различных натуральных чисел, не превышающих 10 ** 9, в порядке возрастания,
# во второй — целое число 1 <= n <= 10**5 и k натуральных чисел b1 ... bk, не превышающих 10 ** 9. Для каждого i от 1 до k необходимо вывести индекс 1 <= j < n, для которого
# A[j] = bi или -1, если такого j нет.

import math
a=[int (i) for i in input().split()]
b=[int (i) for i in input().split()]
aStart=a[1:len(a)]
b=b[1:len(b)]
c=[]

def dihotomy(start,end,element):
    j=int((start+end)/2)
    if element==aStart[j]:
        print(j+1,end = ' ')
    elif end-start==0:
        print(-1,end = ' ')
    elif element>(aStart[j]):
        start=j+1
        dihotomy(start,end,element)
    else:
        end=j
        dihotomy(start,end,element)

for i in range(len(b)):
    dihotomy(0,a[0]-1,b[i])