class Car:
    def __init__(self, make, model):
        self.make = make  # 'self' refers to the instance being created
        self.model = model

    def display_info(self):
        # 'self' refers to the instance that called the method
        print(f"This car is a {self.make} {self.model}")

# Creating two instances of Car
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Calling the display_info method
car1.display_info()  # Output: This car is a Toyota Corolla
car2.display_info()  # Output: This car is a Honda Civic
