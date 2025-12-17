first_dict_keys=input().split()
first_dict_values=input().split()
second_dict_keys=input().split()
second_dict_values=input().split()

dict_list={}
for i in range(len(first_dict_keys)):
   dict_list[first_dict_keys[i]]=int(first_dict_values[i])
for i in range(len(second_dict_keys)):
    dict_list[second_dict_keys[i]]=int(second_dict_values[i])
   
result=sorted(dict_list.items())
print(result)
