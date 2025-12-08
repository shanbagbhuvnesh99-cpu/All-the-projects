import math

while True:
    print("\nWelcome to Calculator!!")

    print("\nPress + for addition")
    print("Press - for subtraction")
    print("Press x for multiplication")
    print("Press / for division")
    print("Press ^2 for square")
    print("Press ^3 for cube")
    print("Press √ for square root")

    operation = input("\nEnter your choice: ")

    if operation in ['+', '-', 'x', '/']:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if operation == '+':
            print(f"The sum is {a + b}")
        elif operation == '-':
            print(f"The difference is {a - b}")
        elif operation == 'x':
            print(f"The product is {a * b}")
        elif operation == '/':
            if b == 0:
                print("Error: Division by zero is not possible.")
            else:
                print(f"The quotient is {a / b}")

    elif operation == '^2':
        a = float(input("Enter the number: "))
        print(f"The square of {a} is {a ** 2}")

    elif operation == '^3':
        a = float(input("Enter the number: "))
        print(f"The cube of {a} is {a ** 3}")

    elif operation == '√':
        a = float(input("Enter the number: "))
        print(f"The square root of {a} is {math.sqrt(a)}")

    else:
        print("Invalid input.")

    again = input("\nDo you want to calculate again? (y/n): ").lower()
    if again != 'y':
        print("Goodbye!")
        break
