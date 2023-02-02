string=str(input("Enter string: "))
a=len(string)
b=[]
b[:0] = string
print(b)
c=[]
j=0
t=""
h=[]

for i in b:
     if(i=='-'):
          c.append(j)
          j=j+1
     else:
          j=j+1

for i in c:
     x=b[i-1]
     y=b[i+1]

     if (x.isalpha()==True and y.isalpha()==True):
          for f in range(ord(x)+1,ord(y)):
               t=t+chr(f)

          b[i]=t


     elif (x.isalnum() == True and y.isalnum() == True):
          x=int(x)
          y=int(y)
          for f in range(x+1,y):
               h.append(f)

          b[i]=' '.join(map(str, h))
     else:
          b.pop(i)

b=' '.join(map(str,b))
print(b)





















