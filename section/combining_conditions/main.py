# The item's discount and stock status have been defined
discounted = False
lowStock = True

# Setting variables
movingProduct = discounted or lowStock
promotion = not discounted and not lowStock

# Output:
print(f"Is the item eligible for promotion? {promotion}")