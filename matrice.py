a=[]
n=int(input('dati dimensiunea matricei ='))
k=[]
e=[]   
f=[]
for o in range(0,n):
    for i in range(0,n):
        x=int(input('Dati elementul='))
        f.extend([x])
a.append(f)

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
        if i+j==n-1:   #n=5 n-1=4
            h.append(a[i][j])
print(h)
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


