# This program reads a text file and prints it as two seperate lists.

# Prints first list title.
print("\033[4m\033[1mName\033[0m\n")

names = []
birthdates = []

with open('DOB.txt', 'r+') as file:
    for line in file:
        words = line.split()
        name = f"{words[0]} {words[1]}"
        birthdate = ' '.join(words[2:5])
        names.append(name)
        birthdates.append(birthdate)

# Prints list of names.
for name in names:
    print(name)

# Prints second list title.
print("\n\033[1m\033[4mBirthdate\033[0m\n")

# Prints list of birthdates.
for birthdate in birthdates:
    print(birthdate)