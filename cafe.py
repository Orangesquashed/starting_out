# This program works out the value of stock in your cafe 

star_pattern = "*" * 50
line_pattern = "-" * 50
print(f"{star_pattern}\n\t\t\tWelcome to Carey's Cafe\n{star_pattern}")

# List of the current menu items
menu = ["Coffee", "Tea", "Hot Chocolate", "Lemonade"]

# Cafe menu items in a dictionary with current stock levels
stock = {
    "Coffee": 100,
    "Tea": 100,
    "Hot Chocolate": 50,
    "Lemonade": 10}

# Cafe menu items in a dictionary with current prices
price = {
    "Coffee": 3.00,
    "Tea": 1.50,
    "Hot Chocolate": 3.00,
    "Lemonade": 2.50}

# Iterates over menu and lists the current stock and prices to 2 decimal places.
def display_menu():
    print("\nOur Current Cafe Menu:")
    for item in menu:
        quantity = stock[item]
        value = price[item]
        print(f"\n{item}:\nStock - {quantity}, Price - £{value:.2f}")

# Iterates over menu, multiplies current stock amounts and prices and stores the value. 
def stock_value():
    total_value = 0
    for item in menu:
        quantity = stock[item]
        value = price[item]
        total_value += quantity * value
    return total_value

# Displays the cafe menu.
display_menu()

# Displays stock value to 2 decimal places.
stock_value = stock_value()
print(f"\n{line_pattern}\nTotal Stock Value: £{stock_value:.2f}\n")