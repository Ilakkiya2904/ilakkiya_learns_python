n=int(input())
stars=1
for i in range(1,n+1):
    spaces=" "*2*(n-i)
    star=(str(i)+" ")*stars
    print(spaces+star)
    stars+=2
