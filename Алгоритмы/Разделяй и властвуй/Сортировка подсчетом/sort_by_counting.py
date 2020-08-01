# Первая строка содержит число 1 <= n <= 10**4, вторая — n натуральных чисел, не превышающих 10. Выведите упорядоченную по неубыванию последовательность этих чисел.

n=int(input())
arr=[int (i) for i in input().split()]
def countsort(Array,LenArray):
    B=[0]*10
    for i in range(LenArray):
        B[Array[i]-1]+=1

    for i in range(1,10):
        B[i]=B[i]+B[i-1]
    
    Array2 = [0]*LenArray
    
    for i in range((LenArray-1),-1,-1):
        Array2[B[Array[i]-1]-1]=Array[i]
        B[Array[i]-1]-=1
        
    for i in range(LenArray):
        print(Array2[i],end=' ')
    
countsort(arr,n)