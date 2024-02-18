# a Python program to square and cube every number in a given list of integers using Lambda.

square  = lambda x: x*x
cube = lambda x : x*x*x

list = [1,2,3,4,5]

sq_list = [square(i) for i in list]
cube_list = [cube(i) for i in list]


print(sq_list)
print(cube_list)
