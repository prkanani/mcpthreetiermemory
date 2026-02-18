def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibonacci_sequence(start, end):
    if start > end:
        start, end = end, start
    return [fibonacci(i) for i in range(start, end + 1)]


def main():
    try:
        start = int(input("Enter the start index (non-negative integer): "))
        end = int(input("Enter the end index (non-negative integer): "))
        if start < 0 or end < 0:
            print("Please enter non-negative integers.")
            return
    except ValueError:
        print("Invalid input. Please enter integers.")
        return

    seq = fibonacci_sequence(start, end)
    print(f"Fibonacci sequence from index {start} to {end}:")
    print(seq)


if __name__ == "__main__":
    main()
