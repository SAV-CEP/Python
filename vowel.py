word=input("Enter a word: ")
vowel="aeiouAEIOU"
vowel_list=[]
for i in word:
    if i in vowel:
        vowel_list.append(i)
print("Vowel list is: ",vowel_list)