numb=[]
n=int(input("Enter the no of elements :"))
for i in range(0,n):
    num=int(input("Enter the number :"))
    numb.append(num)
print("Original list ",numb)
updated_list=[]
for i in range(0,n):
    if i%2==0:
        updated_list.append(numb[i])
print("Updated list ",updated_list)