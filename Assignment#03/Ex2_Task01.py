# You have collected information about cities in your province. You decide to store each city’s
# name, population, and mayor in a file. Write a python program to accept the data for a number
# of
# cities from the keyboard and store the data in a file in the order in which they’re entered.

def myFunction(): # if ki condition ki waja se banaya h 
    city_data = []
    # try:
    #     num_cities = int(input("Enter the number of cities: "))
    #     if num_cities <= 0:
    #         print("Number of cities must be a positive integer.")
    #         return
    # except ValueError:
    #     print("Invalid input. Please enter a valid integer for the number of cities.")
    #     return
    num_cities = int(input("Enter the number of cities: "))
    if num_cities <= 0:
        print("Number of cities must be a positive integer.")
        return

    for i in range(1, num_cities + 1):
        city_name = input("Enter the name of city: ")
        population = input("Enter the population of: ")
        mayor = input("Enter the name of the mayor of: ")

        city_info = {
            'name': city_name,
            'population': population,
            'mayor': mayor
        }
        city_data.append(city_info)

    file_name = "city_data.txt"
    
    with open(file_name, 'w') as file:
        for city in city_data:
            file.write(f"City: {city['name']}, Population: {city['population']}, Mayor: {city['mayor']}\n")
    print(f"City data has been saved to {file_name}.") # f nh likhnge to file_name hi print hojayega asal name nh print hoga




myFunction()
