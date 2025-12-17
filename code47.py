string=input().split()
string_copy=string.copy()

for i in string:
    if string_copy.count(i)>1:
        string_copy.remove(i)

new_list=[]
for i in string_copy:
    msg="{}: {}"
    value=msg.format(i,string.count(i))
    new_list.append(value)
    
for i in sorted(new_list):
   print(i)
