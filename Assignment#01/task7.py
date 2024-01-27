# (ii)Write a Python program to print a specified list after removing the 0th, 4th and 5th elements
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow',’Teapink’]
# Expected Output : ['Green', 'White', 'Black']

list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow','Teapink']

#By remove ----> it remove first appearence
#SYNTAX : .remove(element)
list.remove(list[5])
list.remove(list[4])
list.remove(list[0])


#agr pehle 0 index ko delete krnge to list change hojayegi or index change hojayenge
# del list[5]
# del list[4]
# del list[0]

print (list)