n=input()
s=len(n)
h=0
k=0
for i in n:
    h+=int(i)**s
print(n)
if int(n)==int(h):
    print("yes")
else:
    print("no")


