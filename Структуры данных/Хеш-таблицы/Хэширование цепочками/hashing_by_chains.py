# Вход
# Первая строка размер хеш-таблицы m. Следующая строка содержит количество запросов n. Каждая из последующих n строк содержит запрос одного из перечисленных выше четырёхтипов.

# Выход
# Для каждого из запросов типа find и check выведите результат в отдельной строке.

d={}
m = int(input())
n = int(input())
p = 1000000007


def hashing(word):
    h=0
    for i in range(len(word)):
        h = h + (ord(word[i]) * (263**i))
    h = h%p%m
    return(h)

for i in range(n):
    command,word=input().split(' ')
    if command=='check':
        h=int(word)
        if h in d:
            for i in range(len(d[h])):
                print(d[h][i],end=' ')
            print('')
        else:
            print('')
    else:
        h=hashing(word)
        if command=='add':
            if h in d:
                skip=0
                for i in range(len(d[h])):
                    if d[h][i]==word:
                        skip=1
                        break
                if skip==0:
                    d[h].insert(0,word)
            else:
                d[h]=[]
                d[h].append(word)
        elif command=='del':
            if h in d:
                for i in range(len(d[h])):
                    if d[h][i]==word:
                        d[h].remove(word)
                        break
        elif command=='find':
            skip=0
            if h in d:
                for i in range(len(d[h])):
                    if d[h][i]==word:
                        print('yes')
                        skip=1
                        break
                if skip==0:
                    print('no')
            else:
                print('no')