n=input().split()
new=[]
for i in n:
    i=int(i)
    new.append(i) 
new=set(new)
val=list(new)
print(sorted(val,reverse=False))
