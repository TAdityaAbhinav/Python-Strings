

'''Q. Given two strings.make Str1 equals to Str2 and print the count of number of operations 
      performed during process.
      Ex: I: a3   (aaa)          O: 7
             b4   (bbbb)
'''

def numtostr(k):
    l=len(k)
    s=""
    for i in k:
        if ord(i)>=97 and ord(i)<=122:
            c=i
        else:
            n1=ord(i)                         #order of numbers(1-9): 49-57
            s=(s+c)*(n1-48)
    return s

a=input("Enter your 1st String:")
b=input("Enter your 2nd String:")
a1=numtostr(a)
b1=numtostr(b)
print(a,"to",a1)
print(b,"to",b1)
c=0
for i in range(len(a1)):
    if a1[i]!=b1[i]:                         #1. using REPLACE()= Is used to replace a character in string
        a1=a1[:i]+b1[i]+a1[i+1:]             #2. using Slicing
        c+=2
if len(a1)!=len(b1):
    for i in range(len(a1),len(b1)):
        a1=a1+b1[i]
        c+=1
               
print(a1,b1,"count:",c)

