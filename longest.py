def longest(text):
    words = text.split()
    longest_word = ""

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word

# User input
sentence = input("Enter a sentence: ")


# Display the longest word
print("Longest word:", longest(sentence))