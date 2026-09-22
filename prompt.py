numb=[]
n=int(input("Enter the number of elements:"))
for i in range(0,n):
    ele=int(input("Enter the element:"))
    numb.append(ele)
print("\n",numb)
for i in range(0,n):
    if numb[i]>100:
        numb[i]='Over'
print(numb)