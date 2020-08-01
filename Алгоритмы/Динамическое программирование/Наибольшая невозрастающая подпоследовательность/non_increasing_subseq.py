# Дано целое число 1 <= n <= 10**3 и массив A[1…n] натуральных чисел, не превосходящих 2*10**9. Найдите наибольшую невозрастающую подпоследовательность в A. 
# В первой строке выведите её длину k, во второй — её индексы 1 <= i1 <= i2 <= ... <= ik <= n

n = int(input())
seq = [int (i) for i in input().split()]

parent = [-1]
subseq = [0]
l_abs=0 #Начало подпоследовательности
m_abs=0 #Конец подпоследовательности
for i in range(1,n):
    if seq[i] <= seq[subseq[m_abs]]: # Если элемент заданной последовательности меньше последнего элемента текущей невозрастаюзей подпоследовательности - он является продолжением длиннейшей невозрастающей подпоследовательности
        subseq.append(i) # и добавляется в нее
        parent.append(subseq[m_abs]) #Родителем элемента становится предпоследний элемент в подпоследовательности 
        m_abs += 1 #Индекс последнего элемента подпоследовательности увеличивается на 1
    else:
        l = l_abs
        m = m_abs
        while m>l:
            med = (m+l)//2
            if seq[i] > seq[subseq[med]]:
                m = med - 1
            else:
                l = med + 1
        if (l == 0) & (seq[i] > seq[subseq[l]]):
            parent.append(-1)
            subseq[l] = i
        elif (l == 0) & (seq[i] <= seq[subseq[l]]):
            subseq[l+1] = i
            parent.append(subseq[l])
        elif (l > 0) & (seq[i] > seq[subseq[l]]):
            subseq[l] = i
            parent.append(subseq[l-1])
        elif (l > 0) & (seq[i] <= seq[subseq[l]]):
            subseq[l+1] = i
            parent.append(subseq[l])

ans = []
link = subseq[m_abs]
while link != -1:
    ans.append(link)
    link = parent[link]

print(m_abs+1)
for i in ans[::-1]:
    print(i+1, end=' ')