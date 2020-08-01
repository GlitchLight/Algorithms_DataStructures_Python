# Формат входа. Первая строка содержит число вершин n. Вершины дерева про нумерованы числами от 0 до n−1. Вершина 0 является корнем.
# Каждая из следующих n строк содержит информацию о вершинах 0,1,...,n−1:i-ястрока 
# задаёт числа key i, left i и right i, где key i — ключ вершины i, lefti — индекс левого сына вершины i, а right i — индекс правого сына вершины i. 
# Если у вершины i нет одного или обоих сыновей, соответствующее значение равно−1.

# Формат выхода. Выведите «CORRECT», если дерево является корректным деревом поиска,и «INCORRECT» в противном случае

current_max = -float('Inf')
def is_correct_in_order(root,current_max):
    S=[]
    len_S = 0
    current = root
    
    while True:
    
        while current!=-1:
            S.append(current)
            len_S += 1
            current = tree_lst[current][1]
    
        if (current == -1) & (len_S == 0):
            break
            
        else:
            element = S.pop()
            len_S -= 1
            if tree_lst[element][0] < current_max:
                return False
            else:
                current_max = tree_lst[element][0]
                current = tree_lst[element][2]
    return True

n = int(input())
tree_lst = []
for i in range(n):
    tree_lst.append([int (i) for i in input().split()])

if n>0:
    ans = is_correct_in_order(0,current_max)
else:
    ans = True
    
if ans == True:
    print('CORRECT')
else:
    print('INCORRECT')
