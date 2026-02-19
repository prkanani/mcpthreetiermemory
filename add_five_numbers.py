def add_five_numbers():
    numbers = []
    for i in range(1, 6):
        while True:
            try:
                num = float(input(f"Enter number {i}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    total = sum(numbers)
    print(f"The sum of the five numbers is: {total}")

if __name__ == "__main__":
    add_five_numbers()
