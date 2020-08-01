# Формат входа. Образец Pattern и текст Text.

# Формат выхода. Индексы вхождений строки Pattern в строку Text в возрастающем порядке, используя индексацию с нуля

pattern = input()[::-1]
m = len(pattern)
text = input()[::-1]
l=len(text)
p = 1000000007
x=100
xp=x%p
xi=1
for i in range(m-1):
    xi=(xi*xp)%p
output=[]
loutput=0

h=0
xj=1
for i in range(m):
    h = (h + ord(pattern[i]) * xj)%p
    xj=(xj*xp)%p
hpattern = h #Для паттерна

h=0
xj=1
for i in range(m):
    s = (ord(text[i+(l-m)]) % p * xj)%p
    h = (h + s)%p
    xj=(xj * xp)%p
hwindow = h #Для последнего окна

i=l-1
if hwindow==hpattern:
    print(0,end=' ')            
        
for i in range(l-2, m-2, -1):
    h = (((h - s)%p * xp) % p + ord(text[i-m+1]) % p)%p
    s = (ord(text[i]) % p * xi) % p
    if h==hpattern:
        print(l-i-1,end=' ')
