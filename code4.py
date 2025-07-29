#Write a program that reads a number n and prints the cube of n numbers from 1 
num=int(input())
count=0
counter=1
while(count<num):
    print(counter*counter*counter)
    count=count+1
    counter=counter+1