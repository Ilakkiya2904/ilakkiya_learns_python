#Write a program that reads a number n and prints the sum of squares of n numbers starting from 1
n=int(input("enter the number:"))        
count=0     
add=0 
counter=0
sq=1
while(count<n):
    add=add+1 
    sq=add*add
    counter=counter+sq
    count+=1
print(counter)