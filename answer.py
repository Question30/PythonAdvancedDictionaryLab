# Problem 1
# Add the following key/value pair to the dictionary below. "oceans": ["Pacific", "Atlantic", "Indian", "Arctic"]
geography= {"continets": ["North America", "South America", "Africa", "Antarctica", "Australia", "Asia", "Europe"]}

geography["oceans"] = ["Pacific", "Atlantic", "Indian", "Arctic"]
print(geography)

# Problem 2
# Use the Dictionary below
# Change the value for the height key to 72 inches
patient= {"name": "John Doe", "age": 25, "height": 64, "symptoms": "cough" }
patient["height"] = 72
print(patient)

# Problem 3
# Use the same dictionary as above
# Use a Class method to generate a list of tuples that consists of each key:value pair
print(patient.items())

# Problem 4
# Use the same dictionary as above
# Use a Class method to print the value of "name'
print(patient.get("name"))

# Problem 5
# Use the same dictionary as above
# Use a Class method to look for the key "weight", and supply a default arguement of 150 if the value is not found
print(patient.get("weight", 150))

# Problem 6
# Use the same dictionary as above
# Use a Class method to remove everything from the dictionary
patient.clear()
print(patient)

# Problem 7

# Use the dictionary below
# Use a for loop to move through the dictionary.
# If the value is above 2000, add the value to a new list minus 500
# Example: If the value is 2500, 2000 would be added to the new list
stock_qty= {"cookies": 3200, "bread": 500, "crackers": 52000, "chips": 2000}

new_list = []

for value in stock_qty.values():
    if value > 2000:
        new_list.append(value - 500)

print(new_list)

# *Problem 8 *

# Use the list I did below

# Loop through the list

# Create a dictionary to keep track of how many times a number appears in a list

# Print the final dictionary

# Things to consider:

# How to check if an integer already exists in the new dictionary
# What is the first value when the key gets added to the dictionary?
# How to increase the value of each key on each iteration of the loop?

list= [10, 9, 88, 20, 9, 20, 22, 101, 68, 10, 108, 33, 9, 53]

freq_dict = {}

for item in list:
    if item not in freq_dict:
        freq_dict[item] = 1
    else:
        freq_dict[item] = freq_dict[item] + 1

print(freq_dict)