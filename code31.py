def number_of_cars_needed(no_of_people):
    # Complete this function
    if no_of_people%5==0:
       return (no_of_people//5)
    else:
        return ((no_of_people//5)+1)
      


no_of_people = int(input())
# Call the number_of_cars_needed function
result=number_of_cars_needed(no_of_people)
print(result)
