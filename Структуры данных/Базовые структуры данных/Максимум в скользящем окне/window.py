# Вход. Массив чисел A[1...n] и число 1 ≤ m ≤ n
# Выход. Максимум подмассива A[i... i + m −1] для всех 1 ≤ i ≤ n − m + 1.

n=int(input())
Arr=[[int(i)] for i in input().split()]
m=int(input())
start=0
lastindex=m-1
tree=[]
    
def SiftUp(element,position,k):
    tree[position]=element
    while k!=-1:
        if (tree[position][0] > tree[k][0]):
            tree[position], tree[k] = tree[k], tree[position]
            tree[position][2], tree[k][2] = tree[k][2], tree[position][2]
            position=k
            k=int((position+1)/2)-1
        else:
            break

def SiftDown(element,position):
    tree[position]=element
    k2=(position+1)*2
    k1=k2-1
    while k1<=lastindex:
        if k1==lastindex:
            if (tree[position][0] < tree[k1][0]):
                tree[position], tree[k1] = tree[k1], tree[position]
                tree[position][2], tree[k1][2] = tree[k1][2], tree[position][2]  
                position=k1
            else:
                break
        elif k1<lastindex:
            if (tree[position][0]<tree[k1][0]) or (tree[position][0]<tree[k2][0]):
                if (tree[k1][0]>=tree[k2][0]):
                    tree[position], tree[k1] = tree[k1], tree[position]
                    tree[position][2], tree[k1][2] = tree[k1][2], tree[position][2]  
                    position=k1
                else:
                    tree[position], tree[k2] = tree[k2], tree[position]
                    tree[position][2], tree[k2][2] = tree[k2][2], tree[position][2]  
                    position=k2
            else:
                break
        k2=(position+1)*2
        k1=k2-1
        
for i in range(m):
    Arr[i].append(i)
    Arr[i].append(i)
    tree.append(Arr[i])
    k=int((i+1)/2-1)
    SiftUp(Arr[i],i,k)

print(tree[0][0],end=' ')

for i in range(m,n):
    Arr[i].append(Arr[start][1])
    Arr[i].append(Arr[start][2])
    k=int((Arr[i][2]+1)/2-1)
    if tree[k][0]<=Arr[i][0]:
        SiftUp(Arr[i],Arr[i][2],k)
    else:
        SiftDown(Arr[i],Arr[i][2])
    start+=1
    print(tree[0][0],end=' ')
