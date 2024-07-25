#heloo-----world
#----helloworld
n=input()
for i in n:
    if(ord(i) == 45):
        print("-",end="")
for i in n:        
    if(ord(i) == 45):
        pass
    else:
        print(i,end="")       

##
count=0
ans=""
for i in n:
    if(i=="-"):
        count+=1
    else:
        ans=ans+i
print("-"*count+ans)      

