n=input().split(",")
k=int(input())
r=[]

for i in n:
    r+=[int(i)]
    
val=sorted(r,reverse=True)

print(val[k-1])
