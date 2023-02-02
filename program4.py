n=int(input("Enter number: "))
a=[]


while(n!=0):
    a.append(n%2)
    n=n//2

b=a[::-1]
d = int("".join(map(str, b)))
print("The binary of number is",d)
length=len(b)

print("Inversion can be done from 1 to", length)

start=int(input("Inversion starts from: "))
end=int(input("inversion end at: "))

if(start>length or end>length or start>length):
    print("Enter valid input")

else:
    for z in  range(start-1,end,1):
        if(b[z]==1):
            b[z]=0
        else:
            b[z]=1


e="".join(map(str, b))
print(e)









