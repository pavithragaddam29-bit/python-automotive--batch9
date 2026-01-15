# calculator using the functions
def add(a, b):
    return a + b

def sub(a, b):
    return abs(a - b)

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed"
def calculator_program():

  while True:
    print("\nCalculator Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice in ['1', '2', '3', '4']:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))

        if choice == '1':
            print("Addition of two numbers:", add(a, b))
        elif choice == '2':
            print("Subtraction of two numbers:", sub(a, b))
        elif choice == '3':
            print("Multiplication of two numbers:", mul(a, b))
        elif choice == '4':
            print("Division of two numbers:", div(a, b))
    elif choice == '5':
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")


if __name__ == "__main__":
    calculator_program()
