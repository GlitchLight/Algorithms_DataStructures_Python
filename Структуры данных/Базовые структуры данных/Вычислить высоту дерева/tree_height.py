# Формат входа. Первая строка содержит натуральное число n. Вторая строка содержит n целых чисел parent 0,...,parent n−1.
# Для каждого 0 ≤ i ≤ n−1, parent i — родитель вершины i; если parent i = −1, то i является корнем. Гарантируется,что корень ровно один.
# Гарантируется, что данная последовательность задаёт дерево.

# Формат выхода. Высота дерева.

n=int(input())
tree=[int (i) for i in input().split()]
d={}
height=0

for i in tree:
    if i not in d:
        h=1
        parent=i
        while parent!=-1:
            parent=tree[parent]
            if parent in d:
                h=h+d[parent]
                break
            h+=1
        d[i]=h
    height=max(h,height)
        
print(height)