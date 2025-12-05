def coversion_function(n):
    modified_list=[]
    for i in n:
        i=int(i)
        modified_list+=[i]
    return modified_list




n=input().split(",")
k=int(input())
n=set(n)
n=list(n)
set_n=coversion_function(n)
items=[]
for i in range(len(set_n)):
    for j in set_n:
        n[i]=int(n[i])
        if ((set_n[i]+j)==k):
            items+=[(n[i],j)]
            break 

unique=set()
items.sort()
for a,b in items:
    sorted_pair=tuple(sorted((a,b)))
    unique.add(sorted_pair)
for p in sorted(unique):
    print(p)

