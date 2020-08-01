# Формат входа. Первая строка содержит число вершин n. Вершины дерева пронумерованы числами от 0 до n−1. Вершина 0 является корнем. 
# Каждая из следующих n строк содержит информацию о вершинах 0,1,...,n−1:i-я строка задаёт числа 
# key i,left i и right i, где key i — ключ вершины i, lefti — индекс левого сына вершины i, а righti — индекс правого сына вершины i. 
# Если у вершины i нет одного или обоих сыновей, соответствующее значение равно−1.

# Формат выхода. Три строки: in-order, pre-order и post-order обходы.

n = int(input())

tree_lst=[]
for i in range(n):
    tree_lst.append([int (i) for i in input().split()])

def in_order(element):
    if element[1] != -1:
        in_order(tree_lst[element[1]])
    print(element[0], end = ' ')
    if element[2] != -1:
        in_order(tree_lst[element[2]])

def pre_order(element):
    print(element[0], end = ' ')
    if element[1] != -1:
        pre_order(tree_lst[element[1]])
    if element[2] != -1:
        pre_order(tree_lst[element[2]])        
        
def post_order(element):
    if element[1] != -1:
        post_order(tree_lst[element[1]])
    if element[2] != -1:
        post_order(tree_lst[element[2]])
    print(element[0], end = ' ')
        
in_order(tree_lst[0])
print('')
pre_order(tree_lst[0])
print('')
post_order(tree_lst[0])
print('')
