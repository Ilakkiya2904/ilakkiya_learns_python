#write a program that reads an amount a and prints the minimum number of 5 and 1 rupee notes required for the given amount
#denominations
a=int(input())
v1=int(a/5)
v2=a%5
v3=int(v2/1)
print("5:"+str(v1))
print("1:"+str(v3))