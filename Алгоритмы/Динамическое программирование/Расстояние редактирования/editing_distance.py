# Вычислите расстояние редактирования двух данных непустых строк длины не более 10^2, содержащих строчные буквы латинского алфавита.

def editing_distance(s1,s2):
    m,n = len(s1),len(s2)
    if m>n:
        return (editing_distance(s2,s1))

    previous_line = [i for i in range(n+1)] 
    for i in range(1,m + 1):
        current_line = [0] * (n + 1)
        current_line[0] = i
        for j in range(1, n+1):
            current_line[j] = min(current_line[j-1] + 1, previous_line[j] + 1, 
                                  previous_line[j-1] + (s1[i-1] != s2[j-1]))
        previous_line = current_line
        
    return previous_line[n]

s1 = input()
s2 = input()
print(editing_distance(s1,s2))