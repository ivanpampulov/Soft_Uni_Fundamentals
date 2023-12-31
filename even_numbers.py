# Function to find indices of even numbers in a list
def find_even_indices(numbers):
    even_indices = [i for i, num in enumerate(numbers) if num % 2 == 0]
    return even_indices

input_string = input()
numbers = [int(num) for num in input_string.split(", ")]

even_indices = find_even_indices(numbers)
print(even_indices)