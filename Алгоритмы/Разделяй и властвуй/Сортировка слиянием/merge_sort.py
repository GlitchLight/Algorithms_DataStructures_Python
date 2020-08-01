# Первая строка содержит число 1 <= n <= 10**5. Вторая — массив A[1 ... n], содержащий натуральные числа, не превосходящие 10**9. 
# Необходимо посчитать число пар индексов i <= i < j <= n, для которых A[i] > a[j]. . (Такая пара элементов называется инверсией массива. 
# Количество инверсий в массиве является в некотором смысле его мерой неупорядоченности: 
# например, в упорядоченном по неубыванию массиве инверсий нет вообще, а в массиве, упорядоченном по убыванию, инверсию образуют каждые два элемента.)

n=int(input())
M = [int(i) for i in input().split()]
count=0

def Merge(A,B,lena,lenb):
    Res=[0]*(lena+lenb)
    i=0
    j=0
    o=0
    while True:
        if A[i]<=B[j]:
            Res[o]+=A[i]
            i+=1
            o+=1
            if i==lena:
                for k in range(j,lenb):
                    Res[o]+=B[k]
                    o+=1
                return(Res)
        else:
            Res[o]+=B[j]
            j+=1
            o+=1
            global count
            count+=1*(lena-i)
            if j==lenb:
                for k in range(i,lena):
                    Res[o]+=A[k]
                    o+=1
                return(Res)

def Mergesort(Array,l,r):
    m=int((l+r)/2)
    if l<m:
        return(Merge(Mergesort(M[l:m],l,m),Mergesort(M[m:r],m,r),m-l,r-m))
    else:
        return(Array)
    
Mergesort(M,0,n)
print(count)