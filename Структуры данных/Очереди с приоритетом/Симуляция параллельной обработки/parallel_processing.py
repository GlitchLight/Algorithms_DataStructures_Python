# Формат входа. Первая строка входа содержит числа n и m. 
# Вторая содержит числа t 0, ..., t m − 1, где ti — время, необходимое на обработку i-й задачи. Считаем, что и процессоры, и задачи нумеруются с нуля.

# Формат выхода. Выход должен содержать ровно m строк: i-я (считая с нуля) строка должна содержать номер процессора, который получит i-ю задачу на обработку,и время,когда это произойдёт.

n,m = [int(i) for i in input().split()]
Arr=[int(i) for i in input().split()]

tree=[]
for i in range(n):
    tree.append([0,i])

def SiftDown(position):
    l=(position+1)*2-1
    r=(position+1)*2
    minindex=position
    if l<=n-1:
        if tree[l][0]<=tree[minindex][0]:
            if (tree[l][0]<tree[minindex][0]):
                minindex=l
            else:
                if (tree[l][0]==tree[minindex][0]):
                    if tree[l][1]<tree[minindex][1]:
                        minindex=l
    if r<=n-1:
        if tree[r][0]<=tree[minindex][0]:
            if (tree[r][0]<tree[minindex][0]):
                minindex=r
            else:
                if (tree[r][0]==tree[minindex][0]):
                    if tree[r][1]<tree[minindex][1]:
                        minindex=r
        
    if position!=minindex:
        tree[position],tree[minindex] = tree[minindex],tree[position]
        SiftDown(minindex)
    
def ChangePriority(position,priority):
    print(tree[position][1],tree[position][0])
    tree[position][0]+=priority
    SiftDown(position)
    
for i in range(m):
    ChangePriority(0,Arr[i])
