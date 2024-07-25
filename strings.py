'''
string methods are 
IS ALPHA
IS DIGIT
IS ALLAM
IS UPPER 
IS LOWER
CONVERT INTO LOWER CASE 
CONVERT INTO UPPER CASE
TITLE CASE
SWAP
'''
n=input()
print(n.isalpha())#only true when string contain has alphabets#()will return the answer if we dont give it will return random value or 
print(n.isdigit())#only true when string has only 0-9
print(n.isalnum())#combination of numbers or  alphabets or even bothe then gives true if any special characters then false
print(n.upper())#complete uppercase
print(n.lower())#compelete lowrcase
print(n.capitalize())#only first letter capital
print(n.title())#this gives captial even after the sapce
print(n.swapcase())#upper to lower lower to upper convert 
print(n.strip())#removes first and last spaces
print(n.replace('a','z'))#repalces a with z
print(n.split())
print(n.split('a'))#prints the output in the form of list here we gave a so it prints a letter as space
print(n.isascii())# just return true if input has ascii or no else false
print(n.isnumeric())#
