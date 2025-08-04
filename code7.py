//Write a python program that reads a number n and prints a Right Angled 
//Triangle of N rows and an Inverted Right Angled Triangle of n rows using stars(*)
n=int(input())
lines=2*n
i=1 
for i in range(1,n+1):
    print("* "*i)
for i in range(n,0,-1):
    print("* "*i)
