def log_operation(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Operation: {func.__name__}({', '.join(map(str, args[1:]))} = {result}")
        return result
    return wrapper

class Calculator:
    @log_operation
    def add(self, a, b):
        return a + b

    @log_operation
    def subtract(self, a, b):
        return a - b

    @log_operation
    def multiply(self, a, b):
        return a * b

    @log_operation
    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return a / b

def main():
    calc = Calculator()
    while True:
        print("\nCalculator Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '5':
            break
        
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            
            if choice == '1':
                calc.add(a, b)
            elif choice == '2':
                calc.subtract(a, b)
            elif choice == '3':
                calc.multiply(a, b)
            elif choice == '4':
                calc.divide(a, b)
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")
        except ZeroDivisionError as e:
            print(e)

if __name__ == "__main__":
    main()