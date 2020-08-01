# В первой строке задано два целых числа 1 <= n <= 50000, 1 <= m <=  50000 — количество отрезков и точек на прямой, соответственно.
# Следующие n строк содержат по два целых числа ai, bi (ai <= bi). — координаты концов отрезков. Последняя строка содержит mm целых чисел — координаты точек. 
# Все координаты не превышают 10**8 по модулю. Точка считается принадлежащей отрезку, если она находится внутри него или на границе. 
# Для каждой точки в порядке появления во вводе выведите, скольким отрезкам она принадлежит.

import math
n,m = [int (i) for i in input().split()]
lines=[0]*n

for i in range(n):
    lines[i]=[int (j) for j in input().split()]

points=[int (i) for i in input().split()]
    
l=0

def partition3start(array,l,r):
    m=l
    m1=m
    q=0
    for i in range(l+1,r+1):
        if array[i][0]<array[m][0]:
            array[m1],array[i]=array[i],array[m1]
            m1+=1
            m=i
        elif array[i][0]==array[m][0]:
            m=i
        else:
            q+=1
            break
            
    if (q!=0):
        for i in range(i+1,r+1):
            if array[i][0]<array[m][0]:
                array[m1],array[m+1] = array[m+1],array[m1]
                array[m1],array[i] = array[i],array[m1]
                m1 += 1
                m += 1
            elif array[i][0] == array[m][0]:
                array[m+1],array[m1] = array[m1],array[m+1]
                array[m1],array[i] = array[i],array[m1]
                m += 1
           
    return(m1,m)

def partition3end(array,l,r):
    m=l
    m1=m
    q=0
    for i in range(l+1,r+1):
        if array[i][1]<array[m][1]:
            array[m1],array[i]=array[i],array[m1]
            m1+=1
            m=i
        elif array[i][1]==array[m][1]:
            m=i
        else:
            q+=1
            break

    if q!=0:
        for i in range(i+1,r+1):
            if array[i][1]<array[m][1]:
                array[m1],array[m+1]=array[m+1],array[m1]
                array[m1],array[i] = array[i],array[m1]
                m1+=1
                m+=1
            elif array[i][1]==array[m][1]:
                array[m+1],array[m1]=array[m1],array[m+1]
                array[m1],array[i]=array[i],array[m1]
                m+=1
           
    return(m1,m)  

def quicksort3start(array,l,r):
    while l<=r:
        array[l],array[math.ceil((l+r)/2)]=array[math.ceil((l+r)/2)],array[l]
        m1,m = partition3start(array,l,r)
        if (m1-l)<(r-m):
            quicksort3start(array,l,m1-1)
            l=m+1
        else:
            quicksort3start(array,m+1,r)
            r=m1-1

def quicksort3end(array,l,r):
    while l<=r:
        array[l],array[math.ceil((l+r)/2)]=array[math.ceil((l+r)/2)],array[l]
        m1,m=partition3end(array,l,r)
        if (m1-l)<(r-m):
            quicksort3end(array,l,m1-1)
            l=m+1
        else:
            quicksort3end(array,m+1,r)
            r=m1-1        
            
def dihotomy(lines,linesend,l,r,point):
    globall=l
    globalr=r
    l1=l
    r1=r
    while l<r:
        m=int((l+r)/2)
        if point >= lines[m][0]:
            if point >= lines[m+1][0]:
                l=m+1
            else:
                r=m
                r1=r
                break
        else:
            r=m-1
            r1=r
    
    l=globall
    r=globalr
    
    while l<r:
        m=math.ceil((l+r)/2)
        if point <= linesend[m][1]:
            if point <= linesend[m-1][1]:
                r=m-1
            else:
                l=m
                l1=m
        else:
            l=m+1
            l1=l
  
    if (point>=lines[0][0])&(point<=linesend[globalr][1]) :
        razn=r1-l1
        print(razn+1,end=' ')
    else:
        print(0,end=' ')
        
quicksort3start(lines,0,n-1)
linesend=[0]*n
for i in range(n):
    linesend[i]=lines[i]
quicksort3end(linesend,0,n-1)

for i in points:
    dihotomy(lines,linesend,0,n-1,i)
