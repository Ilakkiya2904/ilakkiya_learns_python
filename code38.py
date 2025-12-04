num_set = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}
# Write your code here

n=list(map(int,input().split()))

num_set=list(num_set)
new=[]

for i in num_set:
    if i not in n:
        new+=[i]
print(sorted(new,reverse=False))
