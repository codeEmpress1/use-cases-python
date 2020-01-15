# Document at least 3 use cases of instance methods
# 1.
# creating a class that can multiply two different numbers
class Multiplier:
    def __init__(self, value):
        self.value = value
    def multiply_by_number(self, num):
        return self.value  * num

# by_2 = Multiplier(2)
# print(by_2.multiply_by_number(10))


# //////////////////////////////////////////////////////////////////////////////////
# 2.
# Creating students objects from student class
class Students:
    def __init__(self, name, department, GP):
        self.name = name
        self.department = department
        self.GP = GP

# INSTANCE METHOD
    def get_grade(self):
        return self.grader(self.GP)

# INSTANCE METHOD
    def create_student(self):
        return f'Welcome {self.name}, your department is {self.department}, your GP is {self.GP} and your class is {self.get_grade()}'

# STATIC METHOD
    @staticmethod
    def grader(gp):
        if gp >= 7:
            yourclass = 'First class'
        elif gp >= 5:
            yourclass = 'Second class'
        elif gp >= 3:
            yourclass = 'Third class'
        else:
            yourclass = 'Adviced to withdraw'
        return yourclass

# student1 = Students('Ade', 'URP', 4.5)
# print(student1.create_student())


# ///////////////////////////////////////////////////////////////////////////////////
# 3.
class Clothe:

    def __init__(self, color, size, style, price):
        self.color = color
        self.size = size
        self.style = style
        self.price = price
        
    def change_price(self, price):
        self.price = price
        
    def calculate_discount(self, discount):
        return self.price * (discount)

    def new_price(self):
        return self.price - self.calculate_discount()   
    
# blouse = Clothe('blue', 'Small', 'Short-sleeve', 100)
# print(blouse.calculate_discount(.3))