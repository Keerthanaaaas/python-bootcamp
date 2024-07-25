n=int(input())
factor=0
for i in range (2,n**2):
    if (n%i==0):
      factor=factor+1
if int(factor)==1:
   print("yes")     
else:
   print("no")
     