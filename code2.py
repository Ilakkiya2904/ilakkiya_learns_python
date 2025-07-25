#Given a number n, Write a Program that reads n numbers as input and print the product of n numbers.
n=int(input())
count=0 
mul=1 
while(count<n):
    num=int(input())
    mul=mul*num 
    count=count+1 
print(mul)