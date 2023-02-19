scores = [12, 47, 30, 29, 19, 35]
high_scores= [score for score in scores if score > 20]
print(high_scores)
"""
To copy each score element in the new list, we write score as our expression, without applying any operation
"""

item_prices = [120, 25, 40]
under_50 = [price for price in item_prices if price < 50]
print(under_50)


websites = ["nytimes.com", "lemonde.fr", "economist.com"]
french = [website for website in websites if website.count(".fr") > 0]
print(french)


book_codes = ["FH2010", "BV1999", "LB2010"]
books_2010 = [code for code in book_codes if code.count("2010") == 1]
print(books_2010)

# ------------------------------------------------
personal_info = {
    'name':'Nana Yaa Adomaa',
    'ID': 10947512,
    'age': 20,
    'home':'Pantang'
}
personal_info['height'] = 67.45 #to add a new key with a value
print(personal_info)

personal_info = {
    'name':'Nana Yaa Adomaa',
    'ID': 10947512,
    'age': 20,
    'home':'Pantang'
}
del personal_info['age'] #to remove a key valued pair
print(personal_info)

print(len(personal_info))
# -------------------------------------------------------

if 'name' in personal_info:
    print('key "name" is in the dictionary')
else:
    print('oops!')

if 'nage' in personal_info:
    print('key "name" is in the dictionary')
else:
    print('oops!')

if 'email' not in personal_info:
    print('the key "email" is not in the dictionary')

new_string = str(personal_info)
print(new_string)

print(type(personal_info))

sorted_keys = sorted(personal_info)
print(sorted_keys) #sort the keys in the dictionary

items = personal_info.items()
print(items)

that_name = personal_info.get('name')
print(that_name)

ourFavFruits = dict([('Papa', 'Pawpaw'), ('Kwame', 'Orange'), ('Kobby', 'Mango')])
print(ourFavFruits)

# ----------------------------------------------------------------

other_info = {
    'email':'Yaadoku@gmail.com',
    'contact': '0502317445'
}
personal_info.update(other_info)
print(personal_info) #updates the dictionary

# product = {'category': 'book',
#            'price': 4.99,
#            'in_shop': True}

# del product['in_shop']
# print(product)

# ---------------------------------------------------------------------
courses = ["thermodynamics", "anatomy", "linear algebra"]
"""
print(courses[-1])
courses[-3]="african studies" #updating the list
print(courses)
"""

del courses[-2] #remove an element with a specific index
print(courses)

# ----------------------------------------

data = ("Nana Yaa", 19, "9th September 2004")
name = data[0]
age = data[1]
date_of_birth = data[2]

print(f"My name is {name},I am {age} years of age. I was born on {date_of_birth}")

# =------------------------------------------------------------

cake_ingredients = ['eggs', 'flour', 'milk','flavour', 'margarine']
print(cake_ingredients[0:2]) #remember the last index will not be part
print(cake_ingredients[1:])
print(cake_ingredients[3:])
print(cake_ingredients[:2])

# We can also use a format with two colons, [start:stop:step] , where step determines how Python steps between start and end.

print(cake_ingredients[1:4:2])
print(cake_ingredients[::2])

name = "Nana Yaa"
for char in name:
    print(char)


countries = ["France", "Ghana", "Germany", "England"]
for country in countries:
    print(country)
    if country == "Germany":
        break

# ----------------------------------------
names = ["Nana", "Ama", "Kwame"]
scores = [95,  75, 50]
grades = ["A", "B+", "D"]

for name, score, grade in zip(names, scores, grades):
    print(f'{name} had {score} percent in the Thermodynamics Exams. She will see grade {grade} in her records.')


# -------------------------------------------
# begining with classes

# class names have their first letter capitalized

class Cars:
    color = "Black"
    print(color)
    brand = "Buggati"

class Phones:
    water_resistant = True
    case_colour = "Pink"
tecno = Phones()
print(tecno.case_colour)
print(tecno.water_resistant)
# Phones is the definition of the class, water_resistant is the variable, tecno is an instance of the class Phones, to access a class variable we use the format class.variable


class Champion:
    name = "Nana"
    age = 19

    def introduce(self):
        print("Hi!")
        print("I am " + self.name) 
Nana = Champion()
Nana.introduce()
# print(Nana.age)

class Fav_Pet:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs
spooky = Fav_Pet("Brown", 4)
print(spooky.color)
print(spooky.legs) 
'''
# In Python, self is a reference to the instance of a class that is being created. When defining a class, the __init__ method is used to initialize the instance of the class. The self parameter is the first parameter of the __init__ method and is used to refer to the instance being created.
# the keyword self is used to access class variables or methods inside the class definition
'''

# class MyFlower:
#     def __init__(self, kind, color):
#         self.kind = kind
#         self.color = color
        
#     def display_color(self):
#         print(self.color)

# flamboyant_flower =MyFlower("Flamboyant", "Orange")
# print(flamboyant_flower.kind)
# flamboyant_flower.display_color()

class MyCar:
    def __init__(self, looks, brand, color):
        self.looks = looks
        self.brand = brand
        self.color = color
    def CarColor(self):
        print(self.color)

Nanas_Car = MyCar("sleek", "Toyota", "black")
print(Nanas_Car.looks)
print(Nanas_Car.brand)
Nanas_Car.CarColor()


# ============================================SENG207================================================
#  SECTION ONE
# 1. Define a class for Person
# 2. Create a person object from the Person class
# 3. Use the constructor method to define attribute for the Person class
# 4. Write a full_name method that returns the full name of the object

'''
there are two ways in doing this: one will use return function (from instruction above) and one will use print function(my trial)'''
# 1st way
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def full_name(self):
        return  self.first_name + ' ' + self.last_name
        
# creating person object
person = Person("Nana Yaa", "Doku-Amponsah")
# printing the full name
print(person.full_name())
print(person.first_name)
print(person.last_name)

# 2nd way

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def full_name(self):
        print(self.first_name + ' ' + self.last_name)

# creating person object
person = Person("Nana Yaa", "Doku-Amponsah")
# printing the full name
print(person.first_name)
print(person.last_name)
person.full_name()

# ===========================================================================
        
class Mum_Pastries:
    def __init__(self, shape, pastry):
        self.shape = shape
        self.pastry = pastry

    def somePastries(self):
        for p in self.pastry:
            print(p)

myChoice = Mum_Pastries("round",["apple", "orange", "strawberry", "Pear"])
myChoice.somePastries()

# -------------------------------------------------------------------
        
class Book_Series:
 def __init__(self, name, books):
    self.name = name
    self.books = books
    self.num_books = len(books)

 def print_name(self):
    print(self.name)    
  
 def print_books(self):
    print(self.books)

hg = Book_Series("Hunger Games", ["The Hunger Games", "Catching Fire", "Mockingjay"])

hg.print_books()
print(hg.num_books)

