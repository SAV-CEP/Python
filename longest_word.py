list=[]
n=int(input("Enter the no of words: "))
for i in range(0,n):
    a=input("Enter a word: ")
    list.append(a)
print(list)
length=len(list)
str=list[0]
for i in range(1,n):
    if (len(list[i])>length):
        str=list[i]
        length=len(str)

print("The largest word:",str)
print("The Length of theword is",length)