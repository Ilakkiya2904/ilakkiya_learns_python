n=input().split()
n=list(n)
unique=[]
values=[]


for i in n:
    if i not in unique:
        unique.append(i)
        
for i in unique:
    if n.count(i)%2==1:
        values.append(int(i))
values.sort()
print(values)
