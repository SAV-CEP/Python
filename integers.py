list1=list(map(int, input("Enter the first list : ").split()))
list2=list(map(int, input("Enter the second list : ").split()))

if len(list1)==len(list2):
    print("Both have same Length")
else:
    print("Both have different Length")

if sum(list1)==sum(list2):
    print("Both have same sum ", sum(list1))
else:
    print("Both have different sum ", sum(list1), sum(list2))

common=set(list1)&set(list2)

if common:
    print("Both have common elements",common)
else:
    print("Both have No common elements")