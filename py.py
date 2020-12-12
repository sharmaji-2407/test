#Finding closest value of a number in an array 

num=int(input("Enter the number of elements do u want:"))
array=[]
for i in range(0,num):
  x=int(input("enter your element:"))
  array.append(x)

find=int(input("enter number to find closest value:"))
results=0
result=abs(find-array[0])
for j in array:
  if abs(find-j)<result:
    result=abs(find-j)
    results=find-j
print("closest value is:",find-results)
print("closest number difference:",results)
