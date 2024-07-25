n=input()
for i in n:
    print(chr( ord(i)+4),end="")
print(ord("-"))   

#x=120+3=123 chr(123)--->| but should print a=97
#y=121+3=124 chr(124)--->} but should print b=98
#z=122+3=125 chr(125)--->~ but should print c=99