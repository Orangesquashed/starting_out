print("Hello world")
favourite_colour = input("What is your favourite colour?: ")

print(f"You've said that your favourite colour is {favourite_colour}\n")

user_entry = input("Would you like to save your favourite colour?: ")

if user_entry == "yes":
    print("This will be saved\n")
else:
    print("This will not be saved")
