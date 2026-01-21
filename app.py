from abc import ABC, abstractmethod

class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicle"""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)

class student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll no. : {self.roll}")
    
class marks(student):
    def __init__(self, name, roll,marks):
        super().__init__(name, roll)
        self.marks = marks
    
    def total(self):
        self.display()
        print(f"total marks: {sum(self.marks)}")

class phone:
    def __init__(self,name):
        self.name = name
    
    def call(self):
        print(f"\ncalling : {self.name}........\ntring tring.......\ntring tring..........\n\n")

class camera:
    def photo(self):
        print("taking photo........\nkhichik...\n")

class smartphone(phone,camera):
    def __init__(self, name):
        super().__init__(name)
    
    def function(self):
        self.call()
        self.photo()
    
class Printable(ABC):
    @abstractmethod
    def print_data(self):
        pass

class Savable(ABC):
    @abstractmethod
    def save(self):
        pass

class Report(Printable, Savable):
    def print_data(self):
        print("Printing report")
    
    def save(self):
        print("Saving report")

obj1 = Report()
obj1.print_data()