# Вход
# add number name, del number, find number
# Первая строка содержит число запросов n. Каждая из следующих n строк задаёт запрос в одном из трёх описанных выше форматов

# Выход
# Для каждого запроса find выведите в отдельной строке либо имя, либо «notfound».

n=int(input())
command=[]
d={}
for i in range(n):
    command.append(input().split(' '))
    if command[i][0]=='add':
        d[command[i][1]]=command[i][2]
    elif command[i][0]=='del':
        if command[i][1] in d:
            d.pop(command[i][1])
    elif command[i][0]=='find':
        if command[i][1] in d:
            print(d[command[i][1]])
        else:
            print('not found')
