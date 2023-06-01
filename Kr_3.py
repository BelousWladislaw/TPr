name = input()

# Split the name into words
words = name.split()

# Capitalize the first, middle, and last names
capitalized_words = [word.capitalize() if i == 0 or i == len(words) - 1 else word for i, word in enumerate(words)]

# Join the capitalized words back into a string
capitalized_name = ' '.join(capitalized_words)

# Print the capitalized name
print(capitalized_name)
