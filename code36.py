n=int(input())
multiples_of_2=[]
multiples_of_3=[]
for i in range(1,n+1):
    multiples_of_2+=[i*2]
    multiples_of_3+=[i*3]
    
new_mul_2=[]

for i in multiples_of_2:
    if i%3!=0:
        new_mul_2+=[i]
print(sorted(new_mul_2))

new=[]

multiples_of_2=set(multiples_of_2)
multiples_of_3=set(multiples_of_3) 

diff_a=multiples_of_2-multiples_of_3
diff_b=multiples_of_3-multiples_of_2 

result=diff_a|diff_b 
print(list(sorted(result)))
