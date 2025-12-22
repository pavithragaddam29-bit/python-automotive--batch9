# Define a class named Dog
class Dog:
    # Constructor method that initializes the Dog object
    def __init__(self, name, age):
        # Instance variables to store the dog's name and age
        self.name = name
        self.age = age

    # Method to make the dog bark
    def bark(self):
        # Return a string with the dog's name and a barking message
        return f"{self.name} barks!"

# Create instances of the Dog class
dog1 = Dog("lucky", 4)  # Create a Dog named lucky, age 4
dog2 = Dog("pandu", 5)  # Create a Dog named pandu, age 5

# Call the bark method on each dog and print the result
print(dog1.bark())  # Output: lucky barks!
print(dog2.bark())  # Output: pandu barks!

