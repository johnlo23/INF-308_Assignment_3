# John Logiudice
# CINF-308 - Fall 2022
# Assignment 3

# This program:
#   Asks the user for a word
#   Saves the word to a file
#   Reads the word from the file
#   Prints the word
#   Prints the total number of characters in the word
#   Prints the total number of unique characters in the word


# Function to count unique characters in a word
def unique_count(f_word):
    # Convert all letters to uppercase to prepare for replace
    f_word = f_word.upper()

    # Initialize Counter
    u_count = 0

    # Loop through the word replacing each letter with a blank
    # so each unique letter is only counted once
    while len(f_word) > 0:
        u_count += 1
        # Replace all occurrences that match the first letter of the word
        # with a blank
        f_word = f_word.replace(f_word[0], '')
    return u_count


# Open a file for writing
file = open('text.txt', 'w')

# Get a word from the user
while True:
    word = input("Please enter one word: ")
    # Check there is at least one character in the word and no spaces
    if len(word) > 0 and word.count(' ') == 0:
        break

# Write the word to a file
file.write(word)

file.close()

# Open the file for reading
file = open('text.txt', 'r')

# Read the contents of the file
file_word = file.read()
file.close()

# Get the length of the word
len_word = len(file_word)

# Get number of unique letters in the word
unique_letters = unique_count(file_word)

# Print the results
print()
print(f"You entered the word {file_word}.")
print(f"The word {file_word} has {len_word} total characters.")
print(f"There are {unique_letters} unique characters in the word {file_word}.")
