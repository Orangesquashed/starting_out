# This program calculates investments and bonds input by the user.

import math

pattern = 50 * "-"
menu = ["Calculate investments", "Calculate bonds", "Exit"]
interest_type = ["Simple", "Compound"]

# Introduces the user to the program and takes their name for personalisation.

name = input(f"""{pattern} 

Welcome to the investment calculator! 

Please start by entering your name: """).capitalize()

while not name.isalpha():
    name = input("Error: Invalid name. Please try again: ")
else:
    print(f"\n{pattern}\nHello {name}! Let's get started!\n{pattern}")

# Asks the user to select an option from the menu items.

print("\nPlease select an option from the menu below:\n")

for i, word in enumerate(menu, 1):
    print(f"{i}. {word}")

# If they do not type 1, 2, 3, or they enter letters, the user will get an error.

while True:
    option = input("\nOption: ")
    try:
        option = int(option)
        if option in {1, 2, 3}:
            break
        else:
            print("\nError: Invalid option. Please try again")
    except ValueError:
        print("\nError: Invalid option. Please try again")

if option == 1:
    print(f"\n{pattern}\nYou have selected: {menu[0]}\n{pattern}")
elif option == 2:
    print(f"\n{pattern}\nYou have selected: {menu[1]}\n{pattern}")
elif option == 3:
    print(
        f"\n{pattern}\nYou have selected: {menu[2]}\n{pattern}\nThank you for using the investment calculator {name}.\nGoodbye!"
    )

# If option 1 is selected.
# Asks the user to input the details needed for the investment calculation.
# If the user enters a letter they will get an error.

if option == 1:
    deposit = input("\nPlease enter the investment amount: £")
    while not deposit.isdigit():
        deposit = input("Error: invalid entry, please try again: £")
    while True:
        interest_rate = input("\nPlease enter the interest rate: ")
        try:
            interest_rate = float(interest_rate)
            break
        except ValueError:
            print("\nError: Invalid option. Please try again: ")
    years = input("\nPlease enter the number of years you are investing: ")
    while not years.isdigit():
        years = input("Error: invalid entry, please try again: ")

# Asks the user which interest type and outputs the answer.
# If the user does not enter 1, 2, or enters a letter they will get an error.

if option == 1:
    print("\nPlease choose which interest type you would like:\n")
    for i, word in enumerate(interest_type, 1):
        print(f"{i}. {word}")
    while True:
        option_two = input("\nOption: ")
        try:
            option_two = int(option_two)
            if option_two in {1, 2}:
                break
            else:
                print("\nError: Invalid option. Please try again")
        except ValueError:
            print("\nError: Invalid option. Please try again")


def simple_interest():
    amount = 0
    ir_div = float(interest_rate) / 100
    int_calc = int(deposit) * (1 + ir_div * int(years))
    amount += int_calc
    return amount


def compound_interest():
    amount = 0
    new_amount = 0
    ir_div = float(interest_rate) / 100
    int_calc = int(deposit) * math.pow((1 + ir_div), int(years))
    amount += int_calc
    new_amount = "{:.2f}".format(amount)
    return new_amount


if option == 1:
    if option_two == 1:
        print(
            f"\n{pattern}\n{name}, your balance after {years} years will be: £",
            simple_interest())
    elif option_two == 2:
        print(
            f"\n{pattern}\n{name}, your balance after {years} years will be: £",
            compound_interest())

# If option 2 is selected
# Asks the user to input the details needed for the bond calculation.
# If the user enters a letter they will get an error.

if option == 2:
    value = input("\nPlease enter the current value of the house: £")
    while not value.isdigit():
        value = input("Error: invalid entry, please try again: ")
    while True:
        bond_interest_rate = input("\nPlease enter the interest rate: ")
        try:
            bond_interest_rate = float(bond_interest_rate)
            break
        except ValueError:
            print("\nError: Invalid option. Please try again: ")
    months = input("\nPlease enter the number of months of repayment: ")
    while not months.isdigit():
        months = input("Error: invalid entry, please try again: ")

    def bond():
        amount = 0
        new_amount = 0
        bond_int_calc = float(bond_interest_rate) / 100
        bond_monthly = float(bond_int_calc) / 12
        bond_calc = (bond_monthly *
                     int(value)) / (1 - (1 + bond_monthly)**(-(int(months))))
        amount += bond_calc
        new_amount = "{:.2f}".format(amount)
        return new_amount

    print(f"\n{pattern}\n {name}, your monthly repayment will be: £", bond())
