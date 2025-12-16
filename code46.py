string=input().split()
if string[1]=="+":
    print(int(string[0])+int(string[-1]))
elif string[1]=="-":
    print(int(string[0])-int(string[-1]))
elif string[1]=="*":
    print(int(string[0])*int(string[-1]))
elif string[1]=="/":
    print(int(string[0])/int(string[-1]))
elif string[1]=="%":
      print(int(string[0])%int(string[-1]))
    
