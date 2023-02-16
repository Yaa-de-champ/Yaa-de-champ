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