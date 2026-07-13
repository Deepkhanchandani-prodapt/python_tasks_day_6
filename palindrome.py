def is_palindrome(s):
    text = s.lower()
    return text == text[::-1]

word =input ("enter a Strings")
if is_palindrome(word):
    print((f'"(word)"is a palindrome.'))
else:
    print(f'"{word}"is not a palindrome')