n=int(input())
for i in range(1,n+1):
    start_star=("* ")*i 
    end_star=("* ")*i 
    spaces=(" ")*(4*(n-i))
    print(start_star+spaces+end_star)
