a=input()                                      #  i :  AdityaIsAGoodBoy
l=len(a)                                       #  o :  aditya is a good boy
b=""
for i in range(l):
   if ord(a[i])>=65 and ord(a[i])<=90:
       k=ord(a[i])+32
       h=chr(k)
       if i==0:
           b=b+h
       else:
           b=b+" "+h
   else:
        b=b+a[i]
        
print(b)
