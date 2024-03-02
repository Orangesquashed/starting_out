# Print the name of the program for users.
print("Hello world")
# Asks the user to unput their favourite colour.
favourite_colour = input("What is your favourite colour?: ")
# Confirms the users input and asks if they would like to save this. 
print(f"You've said that your favourite colour is {favourite_colour}\n")

user_entry = input("Would you like to save your favourite colour?: ")

if user_entry == "yes":
    print("This will be saved\n")
else:
    print("This will not be saved")
