n=int(input())
count=0 
for i in range(1,n+1):
    if(n%i==0):
        count+=1 
if(count>2):
    print("Number has more than 2 factors")
else:
    print("Number doesn't have more than 2 factors")
