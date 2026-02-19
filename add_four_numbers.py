def add_four_numbers(a, b, c, d):
    return a + b + c + d

if __name__ == "__main__":
    print("Enter four numbers to add:")
    num1 = float(input("Number 1: "))
    num2 = float(input("Number 2: "))
    num3 = float(input("Number 3: "))
    num4 = float(input("Number 4: "))

    result = add_four_numbers(num1, num2, num3, num4)
    print(f"The sum of the four numbers is: {result}")
