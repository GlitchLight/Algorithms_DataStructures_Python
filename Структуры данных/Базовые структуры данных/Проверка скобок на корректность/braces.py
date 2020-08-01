# Формат входа. Строка s[1...n], состоящая из заглавных и прописных букв латинского алфавита, цифр, знаков препинания и скобок из множества []{}().

# Формат выхода. Если скобки в s расставлены правильно, выведите строку “Success".
# В противном случае выведите индекс(используя индексацию с единицы) первой закрывающей скобки, для которой нет соответствующей открывающей.
# Если такой нет, выведите индекс первой открывающей скобки,для которой нет соответствующей закрывающей.

s = input().split()
stack = []
l = 0
j = -1
ans = True


def push(element):
    stack.append(element)


def pop(element, j):
    if j == -1:
        return(False, j)
    if ((element == ']') & (stack[j] == '[')) or ((element == ')') &
       (stack[j] == '(')) or ((element == '}') & (stack[j] == '{')):
        stack.pop()
        j -= 1
        return(True, j)
    else:
        return(False, j)

for i in range(len(s[0])):
    if (s[0][i] == '{') or (s[0][i] == '(') or (s[0][i] == '['):
        push(s[0][i])
        j += 1
        if j == 0:
            k = i
    elif (s[0][i] == '}') or (s[0][i] == ')') or (s[0][i] == ']'):
        ans, j = pop(s[0][i], j)
        if ans is False:
            print(i + 1)
            break

if (j == -1) & (ans is not False):
    print('Success')
elif (j != -1) & (ans is not False):
    print(k + 1)