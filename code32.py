def get_even_numbers_count(numbers):
    # complete this function
    c=0
    for i in numbers:
        if int(i)%2==0:
            c+=1 
    return c
            
    


numbers = input().split()
result = get_even_numbers_count(numbers)# call the get_even_numbers_count function
print(result)
