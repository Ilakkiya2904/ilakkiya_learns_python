n=input().split()
length=int(input())
values=[]
for i in n: 
    value=len(i)
    if len(i)==length:
        values.append(i)
    else:
        print(i,end=" ")
