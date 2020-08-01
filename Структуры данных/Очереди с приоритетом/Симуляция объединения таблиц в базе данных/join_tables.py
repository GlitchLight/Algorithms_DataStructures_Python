# Вход
# Формат входа. Первая строка содержит числа n и m — число таблиц и число запросов, соответственно. Вторая строка содержит n целых чисел r1 , ..., rn — размеры таблиц. 
# Каждая из последующих m строк содержит два номера таблиц destination i и source i, которые необходимо объединить.

# Формат выхода. Для каждого из m запросов выведите максимальный размер таблицы после соответствующего объединения.

n,m = [int(i) for i in input().split()]
r = [int(i) for i in input().split()]
maximum=0
tree=[]
for i in range(n):
    tree.append([i,r[i],0])
    maximum=max(maximum,(r[i]))

for i in range(m):
    destination,source=[int(i)-1 for i in input().split()]
    if destination!=source:
        linkd=destination
        while linkd!=tree[linkd][0]:
            linkd=tree[linkd][0]
        
        links=source
        while links!=tree[links][0]:
            links=tree[links][0]
        
        if linkd!=links:
            if tree[linkd][2]>=tree[links][2]:
                tree[links][0]=tree[linkd][0]
                tree[linkd][1]=tree[links][1]+tree[linkd][1]
                tree[linkd][2]=max(tree[linkd][2],tree[links][2]+1)
                maximum=max(maximum,tree[linkd][1])
                print(maximum)
            else:
                tree[linkd][0]=tree[links][0]
                tree[links][1]=tree[links][1]+tree[linkd][1]
                tree[linkd][2]=max(tree[links][2],tree[linkd][2]+1)
                maximum=max(maximum,tree[links][1])
                print(maximum)
        else:
            print(maximum)
    else:
        print(maximum)