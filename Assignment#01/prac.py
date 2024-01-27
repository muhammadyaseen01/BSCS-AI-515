dict1 = {
    "Pakistan" : "Islamabad",
    "India" : "new Delhi",
    "Bangadesh" : "Dhaka",

}

# print(dir(dict1))
print (dict1)

#copy() and del
dict2 = dict1.copy() #aisa krne se dict2 me se delet hoga srf dict1 se nahi
del dict2["India"]
print (dict1)
print (dict2)

dict3 = dict1

del dict3["India"]
print (dict1) # jo dict3 me delete kia wo dict1 se bhi delete qk mene copy nh banai pointer point krwa dia 

#Update

dict1.update({"Canada" : "Tokyo"})
print (dict1)

dict1[97] = "Seat No";

print (dict1)

#keys() and items()

print (dict1.keys())
print (dict1.items()) # return pairs