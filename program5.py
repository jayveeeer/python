number=int(input("enter number of elements in array: "))
array=[]
count=0
for i in range(number):
    b=int(input("Enter array element: "))
    array.append(b)

element=int(input("Enter element to find in array: "))

for i in range(len(array)):
    if(array[i]==element):
        print("The value is present at index",i)
        count+=1
        break;

if(count==0):
    print("Element not present in array")









