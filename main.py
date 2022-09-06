# Open a file for writing
file = open('text.txt', 'w')

# Get a word from the user
word = input("Please enter one word: ")

# Write the word to a file
file.write(word)

file.close()

# Open the file for reading
file = open('text.txt', 'r')

# Read the contents of the file
file_word = file.read()

# Get the length of the word
len_word = len(file_word)

# Print the results
print()
print(f"You entered and save the word {file_word}.")
print(f"The word {file_word} has {len_word} total characters.")

file.close()
