# Base class (Superclass)
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_details(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

# Derived class (Subclass)
class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)  # Call the superclass constructor
        self.num_doors = num_doors

    def display_details(self):
        super().display_details()  # Call the superclass method
        print(f"Number of Doors: {self.num_doors}")

my_car = Car("Toyota", "Camry", 4)
my_car.display_details()
