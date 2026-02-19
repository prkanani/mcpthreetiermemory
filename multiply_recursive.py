def multiply_numbers(numbers, index=0):
    if index == len(numbers):
        return 1
    return numbers[index] * multiply_numbers(numbers, index + 1)

# Example usage:
numbers = [2, 3, 4, 5, 6, 7, 8]
result = multiply_numbers(numbers)
print(f"The product of {numbers} is {result}")
