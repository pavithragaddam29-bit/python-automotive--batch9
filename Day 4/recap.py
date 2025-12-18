# Get user input
name = input("Enter your name: ")  # string input
age = int(input("Enter your age: "))  # integer input
salary = float(input("Enter your salary: "))  # float input

# Print user information using different formatting methods
print("Hello, %s!" % name)  # % formatting
print("You are {} years old.".format(age))  # str.format() formatting
print(f"Your salary is ${salary:.2f}.")  # f-string formatting

# Print multiple values using print() function
print("Name:", name, "Age:", age, "Salary:", salary)

# Use string formatting to print output
print("Name: %s, Age: %d, Salary: %.2f" % (name, age, salary))
print("Name: {}, Age: {}, Salary: {}".format(name, age, salary))
print(f"Name: {name}, Age: {age}, Salary: {salary:.2f}")
