n=int(input())
temp=n 
values=0 
for i in range(1,n+1):
    spaces=" "*(2*(values))
    stars=(str(temp)+" ")*temp 
    print(spaces+stars)
    values+=1 
    temp-=1
