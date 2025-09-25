

s=int(input())
n=int(input())
num=s 

for i in range(1,n+1):
    for j in range(1,i+1):
        print(s,end=" ")
        s+=1 
    print()
