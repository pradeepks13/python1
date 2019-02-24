1.Write a program to take string "Welcome to ksit" and count the number of spaces in the String.

s=input('enter a string\n')
ans=s.count(" ")
print(ans)


2.Write a program which can compute the factorial of a given number using function(recursion).The output should be a comma seperated value in the console.

def factorial(n):
   if n == 1:
       return n
   else:
       return n*factorial(n-1)

num = int(input("Enter a number:"))

if num < 0:
   print("Enter positive number only")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of",num,"is",factorial(num))

3.With a given integer number n write a program to generate an output in the following pattern.If n=3 the output should be of the form 1:1 2:4 3:9

n=int(input("Enter the number"))
i=1
while i<=n:
    print(i,":",i**2)
    i=i+1

4.Write a program that calculates and print the value according to the given formula.q=sqrt(2*c*d)/h

import math
c=float(input('enter the value of c\n'))
d=float(input('enter the value of d\n'))
h=float(input('enter the value of h\n'))

q=math.sqrt(2*c*d)/h
print(q)


5.Write a program to accept a sequence of comma seperated 4 digit binary number as input and check whether they are divisible by 5.

def BinaryToDecimal(n):
    return int(n,2)
a=input("Enter a 4 digit binary number")
b=BinaryToDecimal(a)
if(b%5==0):
    print("the enterd number is divisible by 5")
else:
    print("the given number is not divisible by 5")


6.Write a program which will find all such numbers between 1000 and 3000 such that each digit of a number is an even number.

list = []
for i in range(1000, 3000):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        list.append(s)
print( ",".join(list))


7.Write a program that accepts a sentence for example:"Hello World! 123".Calculate the number of letters and digits in that sequence.

string = input("Input a string\n")
letters=digits=0
for i in string:
    if i.isdigit():
        digits=digits+1
    elif i.isalpha():
        letters=letters+1

print("Number of Letters=", letters)
print("Number of Digits=", digits)


8.Write a program that accepts a String and count the number of uppercase and lowercase letters in it.

string=input("Enter the string")
count1=0
count2=0
for i in string:
    if(i.islower()):
        count1+=1
    elif(i.isupper()):
        count2+=1
print("The number of lower case characters are:",count1)
print("Number of upper case characters are:",count2)

9.Write a program that computes the amount of a bank account based on a transaction law from console input.The transaction format is D 100 W 100 where D is deposit and W is withdraw.


netamt=0
while True:
    line=input(" ").split()
    if not line:
        break
    amt=int(line[1])
    if line[0]== 'D':
        netamt+=amt
    elif line[0]=='W':
        netamt-=amt
print(netamt)
