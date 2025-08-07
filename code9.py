n=int(input())
count=0 
for i in range(2,9+1):
    if(n%i==0):
        count+=1 
if(count>=1):
    print("Divisible Number")
else:
    print("Indivisible Number")
