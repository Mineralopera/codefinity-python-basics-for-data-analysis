# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"

# Slicing the items:
candy1 = items[:9]
candy2 = items[11:20]
dry_goods = items[22:]

# Slicing the categories: 
category1 = categories[:11]
category2 = categories[13:]

# Setting the prices: 
bubblegum_price = "$1.50"
chocolate_price = "$2.00"
pasta_price = "$5.40"

# Output:
print(f'We have {candy1} for {bubblegum_price} in the {category1}')
print(f'We have {candy2} for {chocolate_price} in the {category1}')
print(f'We have {dry_goods} for {pasta_price} in the {category2}')