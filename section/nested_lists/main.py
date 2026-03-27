# Creating vegetable list
vegetables = ["tomatoes", "potatoes", "onions"]

# Removing items
vegetables.remove('onions')

# Adding items
vegetables.append('carrots')
vegetables.append('cucumbers')

# Sorting the list alphabetically
vegetables.sort()

# Output
print(f'Updated Vegetable Inventory: {vegetables}')

if 'carrots' in vegetables:
    print('Carrots are already in the list.')

if 'cucumbers' in vegetables:
    print('Cucumbers are already in the list.')