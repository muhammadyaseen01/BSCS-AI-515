
# Write a python program to create a data file student.txt and append the message “Now we are
# AI students”s

file_name = "student.txt"

with open(file_name, 'a') as file:
    file.write("Now we are AI students\n")
print("Message appended to",file_name,".")
print(f"Message appended to {file_name}.")

