n=int(input("Enter number: "))
a=[]
c=0

while(n!=0):
    a.append(n%2)
    n=n//2

b=a[::-1]
d = int("".join(map(str, b)))
print("The binary of number is",d)

for z in b:
    if z==1:
        c=c+1
    else:
         continue
print("no of one is", c)


