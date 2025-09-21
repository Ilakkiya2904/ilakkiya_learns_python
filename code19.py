n=int(input())
temp=n
for i in range(1,n+1):
    if i==1:
        print("* "*n)
    elif i==n:
        space=" "*(n-1)
        print(space+"* ")
    else:
        space=" "*(i-1)
        hollow_sp=" "*(2*(n-i)-1)
        print(space+"*"+hollow_sp+"*"+space)
