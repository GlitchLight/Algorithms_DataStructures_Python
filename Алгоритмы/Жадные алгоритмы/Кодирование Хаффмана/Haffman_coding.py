# По данной непустой строке s длины не более 10^4, состоящей из строчных букв латинского алфавита, постройте оптимальный беспрефиксный код. 
# В первой строке выведите количество различных букв k, встречающихся в строке, и размер получившейся закодированной строки. 
# В следующих k строках запишите коды букв в формате "letter: code". В последней строке выведите закодированную строку.

s=input()
d={} # Словарь, в который будут заноситься символы и их частоты

for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
        
d2={} #Словарь, в котором будет написан обратный код Хаффмана для каждого символа
for i in d:
    d2[i] = ''

m=[]

for i in d:
    m.append([d[i],i]) #Начальный массив, для которого будет реализовываться алгоритм Хаффмана
m=sorted(m)

while len(m)>2:
    for i in range(1,len(m[0])):
        d2[m[0][i]]+='0'
    for i in range(1,len(m[1])):
        d2[m[1][i]]+='1'
    m.append([m[0][0]+m[1][0]])
    for i in range(1,len(m[0])):
        m[len(m)-1].append(m[0][i])
    for i in range(1,len(m[1])):
        m[len(m)-1].append(m[1][i])
    del m[1],m[0]
    m=sorted(m)
    
if len(m)==1:
    for i in d2:
        d2[i]+='0'
else:
    if len(m[1])>len(m[0]):
        for i in range(1,len(m[0])):
            d2[m[0][i]]+='0'
        for i in range(1,len(m[1])):
            d2[m[1][i]]+='1'
    else:
        for i in range(1,len(m[0])):
            d2[m[0][i]]+='1'
        for i in range(1,len(m[1])):
            d2[m[1][i]]+='0'
            
s2=''

for i in s:
    s2+=''.join(reversed(d2[i])) #Закодированная исходная строка
    
print(len(d),len(s2))
for key in d2:
    print(key+':',''.join(reversed(d2[key])))
print(s2)
