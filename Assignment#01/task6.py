# (i)Write a list comprehension which, from a list, generates a lowercased version of each string that has
# length greater than five.

#By Loop
list = ['Red', 'green', 'white', 'Black', 'Pink', 'yellow','teapink']
newList = []
for item in list:
    if item.islower() and len(item) > 5:
        newList.append(item)
    
print (list)
print(newList)

#By Using List comprehension
newList2 = [item for item in list if item.islower() and len(item) > 5] 
print (newList2)