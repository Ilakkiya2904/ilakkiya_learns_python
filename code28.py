word=input()
r=""
for i in word:
   r=r+chr(ord(i)+1) 
r=r.replace('!'," ")
print(r)
    
