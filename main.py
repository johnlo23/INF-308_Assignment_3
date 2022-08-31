file = open('text.txt', 'w')

s = "Hello there\n"

file.write(s)

file.close()

file = open('text.txt', 'r')

print(file.read())

file.close()
