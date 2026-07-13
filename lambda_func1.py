numbers = list(map(int, input("Enter a list of integers separated by spaces: ").split()))

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

squared_even = list(map(lambda x: x ** 2, even_numbers))

print("Even numbers:", even_numbers)
print("Squared even numbers:", squared_even)