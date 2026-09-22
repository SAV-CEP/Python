from subprocess import check_output

str=input("Enter a sentence: ")
search=input("Enter a word to be searched: ")
count=0
x=str.split(" ")
for i in x:
    if search in i:
        count=count+1
print("The number occurence is:",count)