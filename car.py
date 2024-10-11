class Car:
    def __init__(self, **kwargs):
        # Set default values for the attributes
        self.make = kwargs.get('make', 'Unknown')  # Default to 'Unknown' if not provided
        self.model = kwargs.get('model', 'Unknown')
        self.year = kwargs.get('year', 0)
        self.color = kwargs.get('color', 'Unknown')

    def drive(self):
        print("This " + self.model + " is driving")

    def stop(self):
        print("This " + self.model + " is stopped")

# Example of creating an instance of Car with keyword arguments
my_car = Car(make='Toyota', model='Corolla', year=2020, color='blue')

# Using the methods
my_car.drive()  # Output: This Corolla is driving
my_car.stop()   # Output: This Corolla is stopped
