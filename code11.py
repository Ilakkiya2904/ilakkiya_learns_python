x=int(input())
n=int(input())
power=1 
base=x 
add=0
for i in range(n):
    sq=base**power
    add=add+sq 
    power+=2
print(add)
