# Формат входа. Первая строка содержит число запросов q. Каждая из последующих q строк задаёт запрос в одном из следующих форматов: push v, pop, or max.
# Формат выхода. Для каждого запроса max выведите (в отдельной строке) текущий максимум на стеке.

n = int(input())
Arr=[0]*n
for i in range(n):
    Arr[i]=input().split()

stack=[-1]*n
stackmax=[-1]*n
j=0

for i in range(n):
    if Arr[i][0]=='push':
        stack[j]=int(Arr[i][1])
        if stack[j]>stackmax[j-1]:
            stackmax[j]=stack[j]
        else:
            stackmax[j]=stackmax[j-1]
        j+=1
    elif Arr[i][0]=='pop':
        stack[j-1]=-1
        stackmax[j-1]=-1
        j-=1
    elif Arr[i][0]=='max':
        print(stackmax[j-1])
