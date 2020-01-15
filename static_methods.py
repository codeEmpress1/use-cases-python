# Document at least 3 use cases of static methods
# 1. For validation that is to check if a particular condition is met E.g to check if an individual is adult
from datetime import date 
class Independent:
    def __init__(self, name, DOB):
        self.name = name
        self.DOB = DOB

    def age(self):
        age = (date.today().year - self.DOB)
        print(date.today)
        if self.is_adult(age):
            return f"You are {age} years old and you are an Adult, you can make decisions for yourself. Cheers!"
        return "You are less than 18, you don't belong to this class. Chill till you are old enough"

    @staticmethod
    def is_adult(age):
        return age > 18


# /////////////////////////////////////////////////////////////////////////////////
# 2. To evaluate .... that 
# All instances of this class would have the same base Area but different heights
import math
class Cylinder:
    def __init__(self, height, diameter):
        self.height = height
        self.diameter = diameter
    
    def volume(self):
        return self.base_area(self.diameter) * self.height

    @staticmethod
    def base_area(d):
        return (d/2) ** 2 * math.pi


# //////////////////////////////////////////////////////////////////////////////////////
# 3.

class Animal(object):
    def __init__(self, name):
        self.name = name
        
    @staticmethod
    def create_animal(name):
        return name
    