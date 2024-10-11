class Car:
    def __init__(self, make, model, year):
        # Assigning values to the object's attributes
        self.make = make
        self.model = model
        self.year = year

# Creating an instance of Car
my_car = Car("Toyota", "Corolla", 2020)

# Accessing the assigned attributes
print(my_car.make)   # Output: Toyota
print(my_car.model)  # Output: Corolla
print(my_car.year)   # Output: 2020
