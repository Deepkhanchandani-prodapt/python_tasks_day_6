def longest(text):
    words = text.split()
    longest_word = ""

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word

# Example
text = "Python is an amazing programming language"
print(longest(text))