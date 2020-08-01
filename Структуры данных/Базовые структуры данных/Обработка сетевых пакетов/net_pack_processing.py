# Формат входа. Первая строка входа содержит размер буфера size и число пакетов n. 
# Каждая из следующих n строк содержит два числа: время arrival i прибытия i-го пакета и время duration i, необходимое на его обработку. 
# Гарантируется, что arrival 1 ≤ arrival 2 ≤ ··· ≤ arrival n. При этом может оказаться, что arrival i − 1 = arrival i. 
# В таком случае считаем, что пакет i−1 поступил раньше пакета i.

# Формат выхода. Для каждого из n пакетов выведите время, когда процессор начал его обрабатывать, или −1, если пакет был отброшен.

size,n = [int (i) for i in input().split()]
Arr=n*[0]
for i in range(n):
    Arr[i]=[int (i) for i in input().split()]

stack=[0]*size
for i in range(size):
    stack[i]=[0,0]
count=0
time=0

if (size>=1)&(n>=1):
    stack[count][0]=Arr[0][0]
    stack[count][1]=Arr[0][0]+Arr[0][1]
    count+=1
    print(stack[count-1][0])
    
for i in range(1,n):
    if count<size:
        if stack[count-1][1]>=Arr[i][0]:
            stack[count][0]=stack[count-1][1]
            stack[count][1]=stack[count-1][1]+Arr[i][1]
        else:
            stack[count][0]=Arr[i][0]
            stack[count][1]=stack[count][0]+Arr[i][1]
        print(stack[count][0])
        count+=1
    else:
        if Arr[i][0]<stack[0][1]:
            print(-1)
        else:
            stack2=[[0,0]]*size
            stack2[count-1][0]=max(Arr[i][0],stack[count-1][1])
            stack2[count-1][1]=stack2[count-1][0] + Arr[i][1]
            for i in range(count-1):
                stack2[i]=stack[i+1]
            for i in range(count):
                stack[i]=stack2[i]
            print(stack[count-1][0])