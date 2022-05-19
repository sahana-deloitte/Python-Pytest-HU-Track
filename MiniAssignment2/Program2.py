#Merging Strings to list
lst1=["Hello ", "take "]
lst2=["Dear", "Sir"]
final_list=list()

for str1 in lst1:
    for str2 in lst2:
        final_list.append(str1+str2)

print(final_list)