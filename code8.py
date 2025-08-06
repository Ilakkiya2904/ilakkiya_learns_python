#write a program that reads two numbers n and k and prints the sum of kth power of all numbers from 1 to N
n=int(input())
k=int(input())
add=0
for i in range(1,n+1):
    sq=i**k 
    add=add+sq
print(add)
