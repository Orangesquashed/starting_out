# This takes a string and outputs it in alternate cases.

string = "The quick brown fox jumped over the lazy dog"
string_two = ""
    
for i in range(len(string)):
# If the index is even, the character is capitalized.
    if i % 2 == 0:
        string_two += string[i].upper()
    else:
        string_two += string[i].lower()
        
print(string_two)

# This takes the same string and outputs each alternate word in alternate cases. 

string_three = string.split()

for i in range(len(string_three)):
# If the index is even, the word is capitalized.
    if i % 2 == 0:
        string_three[i] = string_three[i].upper()
    else:
        string_three[i] = string_three[i].lower()
        
print(" ".join(string_three))




