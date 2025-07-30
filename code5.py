#write a program that reads a number n and prits a right angled triangle of n rows using starts(*)
n=int(input())
count=0 
add=0
while(count<n):
    add=add+1 
    print("*"*add)
    count=count+1