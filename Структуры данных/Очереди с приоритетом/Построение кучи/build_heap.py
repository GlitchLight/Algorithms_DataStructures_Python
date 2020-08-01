# Формат входа. Первая строка содержит число n. Следующая строка задаёт массив чисел A[0], ..., A[n−1].

# Формат выхода. Первая строка выхода должна содержать число обменов m, которое должно удовлетворять неравенству 0 ≤ m ≤ 4n.
# Каждая из последующих m строк должна задавать обмен двух элементов массива A.Каждый обмен задаётся парой различных индексов 0 ≤ i 6= j ≤ n−1. 
# После применения всех обменов в указанном порядке массив должен превратиться в мин-кучу,то есть для всех 0 ≤ i ≤ n−1 должны выполняться следующие два условия: 
# • если 2i + 1 ≤ n−1,то A[i] < A[2i + 1]. 
# • если 2i + 2 ≤ n−1,то A[i] < A[2i + 2].

n=int(input())
Arr=[int(i) for i in input().split()]
m=[0]
elements=[]

def BuildHeap(Array):
    for i in range(int((n+1)/2)-1,-1,-1):
        SiftDown(i)

def SiftDown(i):
    minindex=i
    l=(i+1)*2-1
    if (l<=n-1):
        if (Arr[l]<Arr[minindex]):
            minindex=l
    r=(i+1)*2
    if (r<=n-1):
        if (Arr[r]<Arr[minindex]):
            minindex=r
    if i!=minindex:
        elements.append([i,minindex])
        Arr[i],Arr[minindex] = Arr[minindex],Arr[i]
        m[0]+=1
        SiftDown(minindex)
        
BuildHeap(Arr)
print(m[0])
for i in elements:
    print(i[0],i[1])
