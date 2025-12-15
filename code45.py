students_dict = {
    "Ram": "Cricket",
    "Naresh": "Football",
    "Vani": "Tennis",
    "Rahim": "Cricket"
}

# Write your code here
value=input().split() 
students_dict[value[0]]=value[1]
print(students_dict)
