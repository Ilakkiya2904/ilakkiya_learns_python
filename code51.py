matrix=[]
for i in range(3):
    row=input().split()
    matrix.append(row)
win=""
for i in range(3):
    if matrix[i][0]== matrix[i][1]== matrix[i][2] !=' ':
        win=matrix[i][0]
    elif matrix[0][i]==matrix[1][i]==matrix[2][i] !=' ':
        win=matrix[0][i] 

if matrix[0][0]==matrix[1][1]==matrix[2][2]!=' ':
    win=matrix[0][0]
if matrix[0][2]==matrix[1][1]==matrix[2][0]!=" ":
    win=matrix[0][2]
full=all(cell !=' ' for row in matrix for cell in row)
if win=="O":
    print("Abhinav Wins")
elif win=="X":
    print("Anjali Wins")
elif full:
    print("Tie")

