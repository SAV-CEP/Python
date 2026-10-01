d1={}
d2={}
n1=int(input("Enter the number of elements in the first dictionary: :"))
n2=int(input("Enter the number of elements in the second dictionary: :"))
for i in range(n1):
    key=input("Enter the key of the element in the first dictionary: :")
    val=input("Enter the value of the element in the first dictionary: :")
    d1[key]=val
for i in range(n2):
    key=input("Enter the key of the element in the second dictionary: :")
    val=input("Enter the value of the element in the second dictionary: :")
    d2[key]=val
print(d1)
print(d2)
d1.update(d2)
print("Merged Dictionary : ",d1)