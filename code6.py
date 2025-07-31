#write a program to print the factorial of n.
num=int(input())
mul=1 
for _ in range(num):
    mul=mul*num
    num-=1 
print(mul)