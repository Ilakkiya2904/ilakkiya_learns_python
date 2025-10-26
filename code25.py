m=int(input())
n=int(input())

spaces=2*n-3
string="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

index=0 

for i in range(m):
    each_row=""
    
    for j in range(n):
        if i==0 or i==m-1:
            each_row=each_row+string[index]+" "
        elif j==0:
            each_row=each_row+string[index]+" "*spaces+string[n+index-1]
        index=index+1 
    print(each_row)
