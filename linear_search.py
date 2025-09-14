from datetime import datetime
def linear_search_marketplace(products, target_name):

    # Performs a linear search over a list of product dictionaries using for loop
    for product in products:
        if product['name'].lower() == target_name.lower():
            return product  # Found the item
    return None  # Not found

# Products List (Usually this will be on a database)
marketplace_products = [
    {"id": 101, "name": "Wireless Mouse", "price": 25.99},
    {"id": 102, "name": "Bluetooth Speaker", "price": 45.50},
    {"id": 103, "name": "Coffee Mug", "price": 12.00},
    {"id": 104, "name": "Standing Desk", "price": 210.00}
]

# Gets user input to perform a search
productname =  input("Enter the Product Name for look up: ")

# Perform linear search
result = linear_search_marketplace(marketplace_products, productname)

# Output result
if result:

    print("Product found:", result)
else:
    print("Product not found.")

# Print System time
current_time = datetime.now()
print("Execution Time: ",current_time)
