#write a program for consonant
n="My NAme is KEerthana"
a="aeiou"
m="bcdfghjklmnpqrstvwxyz"
count=0
c=0
k=n.lower()
for i in k:
    if i in a:
        count+=1
    elif i in m:
        c+=1
print(count)    
print(c)
