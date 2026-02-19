def multiply_recursive(numbers, index=0):
    """Recursively multiply a list of numbers starting from the given index."""
    if index == len(numbers) - 1:
        return numbers[index]
    return numbers[index] * multiply_recursive(numbers, index + 1)

# Example usage for 7 numbers
numbers_to_multiply = [2, 3, 4, 5, 6, 7, 8]
result = multiply_recursive(numbers_to_multiply)
print(f"Multiplication of {numbers_to_multiply} is {result}")

def add_two_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b

# Example usage for adding two numbers
sum_result = add_two_numbers(10, 20)
print(f"Sum of 10 and 20 is {sum_result}")