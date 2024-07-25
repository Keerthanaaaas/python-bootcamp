'''
check how many vowels are there in string
'''
n=input()
count=0
for i in n:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" :
       count+=1
print (count) 

n="my name is "
a="aeiou"
c=0
for i in n:
    