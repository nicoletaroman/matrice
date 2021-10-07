a=[]
n=int(input('dati dimensiunea matricei ='))
if n>=2 and n<=10:  
    for i in (0,n):
        k=int(input('dati elementele='))
        a.append([k])

print(a)
g=[]
for i in range(len(a)):
    for j in range(len(a[0])):
        if i==j:
            g.append(a[i][j])
print('suma diag. principala este=',sum(g))
h=[]
for i in range(len(a)):
    for j in range(len(a[0])):
        if i+j=n-1:   #n=5 n-1=4
            h.append(a[i][j])
print('suma diag. secundara este=',sum(h))
u=[]
for i in range(len(a)):
    for j in range(len(a[0])):
        if i<j:
           u.append(a[i][j]) 
print('suma elementelor de deasupra diagonalei principale=',sum(u))
l=[]
for i in range(len(a)):
    for j in range(len(a[0])):
        if i<j:
           l.append(a[i][j]) 
print('suma elementelor de deasupra diagonalei principale=',sum(l))
m=[]
for i in range(len(a)):
    for j in range(len(a[0])):
        if i+j<n-1:
           m.append(a[i][j]) 
print('suma elementelor de deasupra diagonalei principale=',sum(m))
y=[]
for i in range(len(a)):
    for j in range(len(a[0])):
        if i+j>n-1:
           y.append(a[i][j]) 
print('suma elementelor de deasupra diagonalei principale=',sum(y))


