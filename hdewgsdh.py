n=input()
s=int(input())
for i in n:
    if (65<=ord(i)<=90):
       print(chr( ord(i)+s),end="")
