## CÂU 3
# initialize dictionaries
amounts = {'HP': 20, 'DELL': 50, 'MACBOOK': 12,	'ASUS': 30}
prices = {'HP': 600, 'DELL': 650, 'MACBOOK': 1200, 'ASUS': 400}

## Get user input
brand = input("input a brand: ")
amount = int(input("input amount to buy: "))

# print total price
total_price = prices[brand]* amount
print("Total price: ", total_price)

# update dictionary & print
amounts[brand] -= amount
print("Available products")
print(f"- {brand}: {amount}")

import random
random.uniform(0.0, 1.0)