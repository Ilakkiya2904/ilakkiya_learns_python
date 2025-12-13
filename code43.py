def get_principal_diagonal_elements(matrix, m, n):
    # Write your code here
    diagonal_list=[]
    for i in range(m):
        if i<n:
            diagonal_list.append(matrix[i][i])
    print(diagonal_list)
        
    

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

# Call the get_principal_diagonal_elements function
get_principal_diagonal_elements(num_list,m,n)
