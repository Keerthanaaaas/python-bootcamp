n=input()
number="0123456789"
m=0
for i in n:
    if i in number:
        print(ord(i),end=" ")
        m += ord(i)
print(m)       
