def conversion_function(n):
    modified_list=[]
    for i in n:
        num=int(i)
        modified_list.append(num)
    return modified_list


n=input().split(",")
r=int(input())

coverted_list=conversion_function(n)

rotate_val=r%len(coverted_list)

first_shift=coverted_list[:rotate_val]
second_shift=coverted_list[rotate_val:]
second_shift.extend(first_shift)
print(second_shift)
