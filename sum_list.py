list=[]
n=int(input('Enter the limit : '))
for i in range(0,n):
    num=int(input('Enter number : '))
    list.append(num)
print(list)
sum=0
for i in range(0,n):
    sum=sum+list[i]
print("The sum is :",sum)