n=int(input())
no_of_test_cases=int(input())
number_list=[]
count=0

for i in range(n):
    num=int(input())
    number_list+=[num]
    
for i in range(1,no_of_test_cases+1):
    k=int(input())
    print(number_list[k])
        
