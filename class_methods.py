# Document at least 3 use cases of class methods
# 1. Creating instance of an object from class methods for example creating different classes of foods

class Books:
    def __init__(self, title , pages, author, edition):
        self.title = title
        self.pages = pages
        self.author = author
        self.edition = edition
    @classmethod
    def create_book(cls, title, pages, author, edition):
        book_details  = f"{title} has {pages} pages, it was written by {author} and this is the {edition} edition." 
        return book_details

#2
class Food:
    @classmethod
    def carbohydrate(cls, food):
        carbohydrate_food = ['Rice', 'Yam', 'Spag']
        if food in carbohydrate_food:
            return f"{food} is an example of carbohydrate."
        else:
            f"{food} is not an example of protein"
    
    @classmethod
    def protein(cls, food):
        return f"{food} is an example of protein."

# Rice = Food.carbohydrate("Rice")
# print(type)

# 3 Creating instances from classmethods
class Animal(object):
    def __init__(self, name):
        self.name = name
    @classmethod
    def create_animal(cls, name):
        return cls(name)

