n=int(input())
for i in range(1,n+1):
    left_sp=" "*(n-i)
    if(i>2) and (i<n):
        hollow_sp=" "*(2*(i-2))
        numbers="1 "+hollow_sp+(str(i)+" ")
        print(left_sp+numbers)
    else:
        numbers=""
        for j in range(1,i+1):
            numbers=numbers+(str(j)+" ")
        print(left_sp+numbers)
