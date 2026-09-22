list=[]
n=int(input("enter the number of elements in the list :"))
for i in range(0,n):
    numb=int(input("Enter the elements in the list :"))
    list.append(numb)
print("The square of the elements in the list :")
for i in range(0,n):
    print(list[i]**2)