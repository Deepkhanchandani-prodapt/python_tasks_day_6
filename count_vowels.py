def count_vowels(text):
    vowels = "aeiou"
    count = 0

    for ch in text.lower():
        if ch in vowels:
            count += 1

    return count

# Example
text = "Hello World"
print(count_vowels(text))