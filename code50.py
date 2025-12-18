string=input().split()
unique=[]

for i in string:
    if i not in unique:
        unique.append(i)
        
for i in unique:
    msg="{}: {}"
    print(msg.format(i,string.count(i)))
