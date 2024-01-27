##(ii) Write a Python program to convert temperatures to and from celsius,
##Fahrenheit.
##Formula : c/5 = f-32/9
##Expected Output :
##Enter temp in Celsius: 60°C
##Temperature in Fahrenheit is :140


#c = 60
celsius = float(input("enter temperature in celsius: "))

#Formula:
fahrenheit = celsius*(9/5)+32

print("Entered Temperature in Celsius is: ",celsius)
print("Temperature in Fahrenheit is: ", fahrenheit)
