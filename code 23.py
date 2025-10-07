n=int(input())
count=0 

for i in range(1,n+1):
    div=False
    for d in range(2,11):
        if i%d==0:
            div=True 
            break
    if not div:
        count+=1 
print(count)

        
