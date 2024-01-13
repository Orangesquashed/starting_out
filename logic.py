# A program where the user can input the month and it tells them how many days it has. 

print("Welcome to the Days in a Month Calculator!\n")

# Months and days are stored in this variable.
month = [['january', 31], ['february', 28], ['march', 31], ['april', 30], ['may', 31], ['june', 30], ['july', 31], ['august', 31], ['september', 30], ['october', 31], ['november', 30], ['december', 31]]

# Asks the user for a month, in lowercase. 
user_input = input("Enter the month in full, all lower case: ")

# Iterates over the list of months and prints the number of days in that month.
for i in range(len(month)):
    if user_input == month[i][0]:
        print(month[i][0])

# The program has a logic error. 