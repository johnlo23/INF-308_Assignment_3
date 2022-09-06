# Open a file for writing
file = open('text.txt', 'w')

# Get a word from the user
word = input("Please enter one word: ")

# Write the word to a file with a trailing newline character
file.write(word + "\n")

file.close()

# Open the file for reading
file = open('text.txt', 'r')

# Read the contents of the file
file_word = file.read()

print(f"You entered and save the word {file_word}")

file.close()
