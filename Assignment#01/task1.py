##(i)Write a Python program to swap 4 variables values (input four values.
##Sample input:
##Before swapping
##a=2,b=56,c=78,d=9
##After Swapping
##a=,9,b=78,c=56,d=2
##

a = 2
#a=input("Enter any  number for a:")
b = 56
#b=input("Enter any number for b:")
c = 78
#c=input("Enter any number for c:")
d = 9
#d=input("Enter any number for d:")

#swapping
a,d=d,a
b,c=c,b
#print("The swapped value of a and d is:",a,d)
#print("The swapped value of b and c is:",b,c)
#print("--------------")
print ("a = ",a," b = ",b, " c = ",c," d = ",d)
