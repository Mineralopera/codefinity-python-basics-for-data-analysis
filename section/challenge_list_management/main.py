# Initializing lists
meat = ['Ham', 3.99, 50, 'Sliced']
cheese = ['Cheddar', 5.49, 100, 'Sharp']
condiment = ['Mustard', 1.99, 75, 'Spicy']

# Creating main list:
deli_dept = [meat, cheese, condiment]

# Printing initial output
print(f'Initial Deli List: {deli_dept}')

# Restocking item
if 'Ham' in meat and meat[2] < 100:
    meat[2] = 100

# Adding seasonal meat
seasonal_meat = ['Turkey', 4.50, 100, 'Sliced']
deli_dept.append(seasonal_meat)

# Removing condiment
deli_dept.remove(condiment)

# Sorting the main list
deli_dept.sort()

# Output
print(f'Updated Deli List: {deli_dept}')