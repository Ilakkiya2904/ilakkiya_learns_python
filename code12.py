n=int(input())  
temp=n
value=0
for i in range(1,n+1):
    spaces=" "*(value)
    stars=((str(temp))+"")*temp 
    print(spaces+stars)
    temp-=1
    value+=1
