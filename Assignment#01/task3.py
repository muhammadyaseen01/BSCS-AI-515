# Append
fruit = ['Mango','Apple','Orange','Pineapple'];
print (fruit);
fruit.append('Guava');
print (fruit);
veg = ['Potato','Onion','Tomato'];
fruit.append(veg)
print(fruit) #append use krne se nested list print horhi
print("------------------------------")
#Extend :  ye break krdeta h value ko string hoga to letters me break list h to elements me break
fruits = ['Mango','Apple','Orange','Pineapple']
print(fruits)
fruits.extend('Guava');
print (fruits);
veg1 = ['Potato','Onion','Tomato'] # extend elements me break krta h to nested list nh banegi
fruits.extend(veg)
print (fruits)

print("------------------------------")
# Insert

list = ['Dell',"Hewlett Packard",'lenovo']
# .insert(index,element)
print(list)
list.insert(0,'apple')
print(list)


print("------------------------------")
#Remove
# .remove(element)
abc = [1, 2 ,3 ,4 ,5]
abc.remove(3)
print(abc)
# abc.remove(31) #give value error if element is not in the list
# print(abc)


print("------------------------------")
# Reverse
newList = [1,2,3,4,5]
print(newList)
newList.reverse()
print(newList)
