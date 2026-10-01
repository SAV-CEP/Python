str=input("Enter the sirng ")
if str[-3:]=='ing':
    str=str+"ly"
else:
    str=str+'ing'

print("The new string is",str)