dict1 = {
    "Pakistan" : "Islamabad",
    "India" : "new Delhi",
    "Bangadesh" : "Dhaka",

}
dict2 = {
    "Canada" : "Toronto",
    "Japan" : "Tokyo"
}

dict1.update(dict2)
# dict1.extend(dict2)
print(dict1)

#operator method
dic = {**dict1,**dict2}
print(dic)

dic1 = dict1 | dict2
print(dic1)

