n=int(input())
value=1
temp=n
for i in range(1,n+1):
    if i==1:
        space=" "*(n-i)
        print(space+"*"+space)
    else:
        space=(n-i)
        hollow_sp=2*(i-2)
        value+=2
        print(" "*space+"* "+" "*hollow_sp+"* ") 

for i in range(2,n+1):
    if i==n:
        space=(n-1) 
        print(" "*space+"* ")
    else:
        space=" "*(i-1) 
        hollow_sp=" "*(2*(n-i)-1)
        print(space+"*"+hollow_sp+"*")
