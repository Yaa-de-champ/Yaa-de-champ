# to remove a value at a specific index


# BMEN_names = ["James", "Cecil", "Safiu", "Nana"]
# BMEN_names.pop(1)
# print(BMEN_names)

# pets = ["snake", "cat", "puppy" ]
# removed = pets.pop(2)
# print(removed)

# using split
# words = "there is a fault now"
# words_list = words.split()
# print(words_list)

# user = "Lauren,25,F,Architect"
# user_1 = user.split(",")
# print(user_1)

# in some special case functions that return boolean values often start with "is" and functions that return values often start with verbs 

# def many_values(x):
#     if x < 3:
#         return "Great!!"
#     else:
#         return "too low!"
# print(many_values(2))
# print(many_values(7))

# def add_to_list( list_name, item):
#     list_name = ["tomatoes", "pepper","carrot"]
#     list_name = list_name + item
#     return list_name
# print (add_to_list(list_name, "carrot") )

# def add_to_list(list_name, item):
    
#     list_name = ["tomatoes", "green peas", "pepper"]
#     item = "fish"
#     list_name.append(item)
# print(list_name)
                                 
# add_to_list(list_name, "cabbage")

# y = [3,4,6,7,8]
# x = [1,2]
# y.append(x)
# print(y)

# my_list = "hello world"
# y = [3,4,6,7,8]
# y.append(my_list)    
# # print(y[5])

# x = [1,2,3,4,5,6]
# y = [7,8,9,]
# x.extend(y)
# print(x)

# my_list = ["cabbage", "tomatoes"]
# for item in my_list:
#    print(item)

# def onbord_passengers(bookings):
#     counter = 1
#     while counter <= bookings:
#         print(f"Passenger {counter} on board")
#         counter += 1

# onbord_passengers(4)     

# def display_progress(total_files):
#     for i in range(total_files):
#         print(f"Downloading file {i} out of {total_files}")
# display_progress(3)   

#do not forget to save your work before running 

# def do_countdown(counter):
#     while counter > 0:
#         print(counter)
#         counter -= 1
#     print("Go!")
# do_countdown(3)    

# for a for loop the number in the range() is the number of times the sentence or word will run


# def show_progress(total):
#     for i in range(total):
#         print(f"Install the next update")
# show_progress(3)        

# def display_progress():
#     for i in range(2):
#         print(f"downloading file {i} out of 3")

# display_progress()

# def show_notifications(messages):
#     for i in range(messages):
#         print("Failed to send messages")

# show_notifications(3)

# def halve_prices(cart):
#     for price in cart:
#         print(f"New price: {price/2}")

# cart = [5, 20, 8]
# halve_prices(cart)


# def display_players(team):
#     number = 1
#     for name in team:
#             print(f"Player {number}: {name}")
# team_1 = ["Yaa", "Cecil"]
# team_2 = ["James", "Melissa"]
# display_players(team_1)

# def show_next_track():
#     playlist = ["Montero", "Dinero", "Ginger", "Awesome God"]
#     for track in playlist:
#         print(f"Next up: {track}")
# show_next_track()

#calling a function twice

# def show_next_track(playlist):
#     for track in playlist:
#         print(f"Next up: {track}")
# montero = ["Love", "Industry Baby"]
# black_love = ["Labadi", "Cashout"]
# show_next_track(montero)
# show_next_track(black_love)      

#tuple helps group related pieces of data

# movies = ["Black Panther",  "Heros of Today", 2003, 1998]
# movies_turples = [("Black Panther", 1998), ("Heros of Today", 2003)]

#eg. list(set(the elements))....removes duplicates in a list

# my_data = ("coding", 2022)
# print(my_data)

# use_data = ("Nana_13",) #special case of turple 
# print(use_data)

# a turple can have as many values as we want 
# fishy_data = ("Vertigo", 1998, "A.Acheampong")
# print(fishy_data)


# another way to create a turple is using the built in function



# a = tuple('company')
# print(a)
# x = tuple(range(4))
# print(x)

# a turple is immutable that is one cannot add or modify items once a turple is intialized

# a list uses [] while a tuple uses ()
# for a tuple a single element must also have a comma after it 

# x = (1, 2)
# m = x
# x += (3, 6)
# print(x)  #output will be (1, 2, 3, 6)
# tuples do not use .append and .extend just like a list

# m = 1, #m is a tuple(1,)
# m = 1 #m is a value 1
# print(m)

# the comma is very needed

# marks = [("Yaa", 67), ("Cecil",98)] #this is an example of a tuple in a list
# print(marks[0])
# output is ("Yaa", 67)

# marks = [("Yaa", 67), ("Cecil",98)]
# Yaa_score = marks[0]
# print(Yaa_score)

# marks = [("Yaa", 67), ("Cecil",98)]
# for user_marks in marks:
#     print(f"Result: {user_marks}")
# out is Result: ('Yaa', 67)
#        Result: ('Cecil', 98)


# water = [("Hydrogen", 11.19), ("Oxygen", 88.81)]
# print(len(water))
# output is 2 because each tuple is taken as one element 

# tuple2 = (1, 2, 3, 8, 6, 8, 3, 4)
# print(len(tuple2))
# print(max(tuple2))
# print(min(tuple2))
# print(set(tuple2)) #the output removed the duplicate 

# converting a tuple to a list
# list = [1, 2, 3, 5, 8]
# print(tuple(list))
# so the output will be (1, 2, 3, 5, 8)

# we can add two tuples
# tuple1 = (3, 4)
# tuple2 = (1, 2)
# print(tuple1 + tuple2)
# remember a tuple can carry any type of value

# x = (1, 2, 3, 4)
# print(x[0])
# print(x[2])
# # indexing with negative numbers will start numbering from the last
# print(x[-1])
# print(x[-3])

# list = ["mango", "fish", "pineapple"]
# print(list[0])
# print(list[-1])
# # it also worked for list 

# indexing a range of elements
# print(x[:-1])
# print(x[-1:])
# print(x[1:4]) #will be back i dont understand !
#unlike a list we cant update, add, or delete values from tuples
#since tuples are immutable we can use them to store information that shouldn't be modified like a person's name and date of birth

# print("Hello," ,end = " ")
# print("Cecil")

# print("Hi,", end="")
# print("I'm here!")

# def greet(greeting="Nana Yaa"):
#     print(greeting)
# greet()

# def math(calculate="mass of object"):
#     print(calculate)
# math()

# def func(marketlist): 
#     for x in marketlist:
#         print(x)

# func("mangoes",)

# print([3] + [6])
# # prints out a list of 3 and 6
# print("8" + "6")
# # prints out 86
# print(8 + 9)
# # prints out the addition of 8 and 9 which is 17

# import random
# randnum = random.randint(0, 12)
# print("The randomly generated number was - " + str(randnum))
# # prints out the full sentence then prints out a random number between 0 and 12

# import random
# rnum = random.randint(7, 15)
# print("I expected a higher number such as -" + str(rnum))

# print('cabbage', 'carrots', 'fish')
# # prints out a list with space but no comma 

# print('cabbage', 'carrots', 'fish' , sep=', ')
# # prints out a list with space and comma between 

# first, second, *tail, last =[1, 2, 3, 4, 5, 6]
# print(first)
# print(second)
# print(tail)
# print(last)
# output becomes 
# 1
# 2
# [3, 4, 5]
# 6

# numbers = [1, 2, 5, 4, 8]
# print(numbers)
# print(*numbers)
# # output becomes 
# [1, 2, 5, 4, 8]
# 1 2 5 4 8

# print("hi, my name is Nana Yaa.")
# print("hi, my name is Nana Yaa."[::-1])
# output becomes 
# hi, my name is Nana Yaa.
# .aaY anaN si eman ym ,ih

# print(list(range(1, 18)))
# list numbers from 1 through to 18

# print(round(1.4))
# print(round(0.6))
# print(round(7.8))
# print(round(3.3))
# the round function will either round the function up or down depending on what is after the decimal point 

# def marks_data(mark_scores):
#     highest = max(mark_scores)
#     lowest = min(mark_scores)
#     return highest, lowest

# mark_scores = [56, 33, 78, 190]
# data = marks_data(mark_scores)
# print(data)

# def market(items):
#     smallest = items[0]
#     largest = items[3]
#     return smallest, largest

# items =["mangoes", "fish", "cabbage", "groundnut"]
# list = market(items)
# print(list)


# results = 44
# if results >= 70:
#     print("GOOD JOB!")
# else:
#     print("more room needed for improvement")


# results = 22
# if results >= 60:
#     print("you made it to the next stage")
# elif results <= 40:
#     print("sorry you can make it to the next stage")
# else:
#     print("still got more work to do")
    

# results = 40.1
# if results >= 60:
#     print("you made it to the next stage")
# elif results <= 40:
#     print("sorry you can make it to the next stage")
# else:
#     print("still got more work to do")
    
# results = 6.7
# if results >= 60:
#     print("you made it to the next stage")
# elif results <= 40:
#     print("sorry you can make it to the next stage")
# else:
#     print("still got more work to do")
    
# results = 55
# if results >= 60:
#     print("you made it to the next stage")
# elif results <= 40:
#     print("sorry you can make it to the next stage")
# else:
#     print("still got more work to do")
    
# results = 45
# if results >= 60:
#     print("you made it to the next stage")
# elif results <= 40:
#     print("sorry you can make it to the next stage")
# else:
#     print("still got more work to do")



# def marks_data(mark_scores):
#     highest = max(mark_scores)
#     lowest = min(mark_scores)
#     return highest, lowest

# mark_scores = [56, 33, 78, 190]
# data = marks_data(mark_scores)
# # print(data)

# highest = data[0]
# smallest = data[1]
# print(f"smallest score: {smallest}")
# print(f"highest score: {highest} ")


def get_top_three(bballplayers):
    return bballplayers[0],  bballplayers[1], bballplayers[2]

bballplayers = ["Cecil", "Randy", "Dave", "William"]
top_three = get_top_three(bballplayers)

print(f"First: {top_three[0]}")
print(f"Second: {top_three[1]}")
print(f"Third: {top_three[2]}")