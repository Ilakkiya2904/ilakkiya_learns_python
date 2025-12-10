def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


m, n = input().split()
m, n = int(m), int(n)
num_list = []

for i in range(m):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)

# Write your code here
max_list=[]
min_list=[]
sum_list=[]

for i in num_list:
    max_list.append(max(i))
    min_list.append(min(i))
    sum_list.append(sum(i))
    
print(max(max_list))
print(min(min_list))
print(sum(sum_list))
    
