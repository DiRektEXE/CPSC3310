# Vajaran Nall

# Ask user for filename
filename = input("Enter the name of an input file: ")

# Open the file for reading
with open(filename, "r") as file:
    contents = file.read()
    words = contents.split()

    unique_words = set(words)

    word_counts = {}

    for word in unique_words:
        word_counts[word] = words.count(word)

    # Header for formatted output

    print("Word           Occurrences")
    print("--------------------------")

    # Loop through the dictionary, print each word and its count 
    for i in word_counts:
        print(f"{i:<15}{word_counts[i]}")