list=[]
n=int(input("Enter the number of elements in the list :"))
for i in range(0,n):
    element=int(input("Enter the element :"))
    list.append(element)
post=[]
for i in range(0,n):
    if list[i]>0:
        post.append(list[i])
print("The positive numbers are:")
print(post)
