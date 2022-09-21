# Python quizzes

from mimetypes import common_types
from statistics import mode
import numpy as np
import pandas as pd
import time

############################################################################################################################# 

# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
rainfall = rainfall*0.9
# add the rainfall variable to the reservoir_volume variable
both = rainfall + reservoir_volume
# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
new_reservoir_volume = reservoir_volume*1.05
# decrease reservoir_volume by 5% to account for evaporation
new_reservoir_volume_evap = reservoir_volume*0.95
# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume_piped = reservoir_volume - 2.5e5
# print the new value of the reservoir_volume variable
print(reservoir_volume_piped)

## #####################

# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions of people.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5

# elements = {"hydrogen": 1, "helium": 2, "carbon": 6}

population = {"Shanghai": 17.8, "Istanbul": 13.3, "Karachi": 13.0, "Mumbai": 12.5}

print(population)

## #####################

## Quiz 1: Fruit basket - Task 1
# You would like to count the number of fruits in your basket.
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# print(basket_items.items())

#Iterate through the dictionary
for fruit, count in basket_items.items():
    #if the key is in the list of fruits, add the value (number of fruits) to result
    if fruit in fruits:
            result += count

print(result)

## #####################

## Quiz: Fruit Basket - Task 3
# You would like to count the number of fruits in your basket.
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for item, count in basket_items.items():
    #if the key is in the list of fruits, add the value (number of fruits) to result
    if item in fruits:
        fruit_count += count
    else:
        not_fruit_count += count
#if the key is in the list of fruits, add to fruit_count.

#if the key is not in the list, then add to the not_fruit_count


print(fruit_count, not_fruit_count)

################################## 

check_prime = [26, 39, 51, 53, 57, 79, 85]

# iterate through the check_prime list
for num in check_prime:

# search for factors, iterating through numbers ranging from 2 to the number itself
    for i in range(2, num):

# number is not prime if modulo is 0
        if (num % i) == 0:
            print("{} is NOT a prime number, because {} is a factor of {}".format(num, i, num))
            break

# otherwise keep checking until we've searched all possible factors, and then declare it prime
        if i == num -1:    
            print("{} IS a prime number".format(num))
            print(" \n ", i)

####################################

# write your function here
def readable_timedelta(days):
    weeks = int(days/7)
    days = days%7
    solution = "{} week(s) and {} day(s).".format(weeks, days)
    return solution

# test your function
print(readable_timedelta(10))

#########################

def create_cast_list(filename):
    cast_list = []
    with open(filename) as f:
        for line in f:
            element = line.split(',', 1)
            # print(element[0])
            cast_list.append(element[0])
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list

    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)

#########################

# initiate empty list to hold user input and sum value of zero
user_list = []
list_sum = 0

# seek user input for ten numbers 
for i in range(10):
    
# check to see if number is even and if yes, add to list_sum
# print incorrect value warning  when ValueError exception occurs
    try:
        userInput = int(input("Enter any 2-digit number: "))
        number = userInput
        user_list.append(number)
        if number % 2 == 0:
            list_sum += number
    except ValueError:
        print("Incorrect value. That's not an int!")

print("user_list: {}".format(user_list))
print("The sum of the even numbers in user_list is: {}.".format(list_sum))


#########################

## Quiz - Generate Random Password

# TODO: First import the `random` module
import random as r

# We begin with an empty `word_list`
word_file = "words.txt"
word_list = []

# We fill up the word_list from the `words.txt` file
with open(word_file,'r') as words:
    for line in words:
        # remove white space and make everything lowercase
        word = line.strip().lower()
        # don't include words that are too long or too short
        if 3 < len(word) < 8:
            word_list.append(word)

# TODO: Add your function generate_password below
# It should return a string consisting of three random words 
# concatenated together without spaces
def generate_password():
    password = word_list[int(r.uniform(0,len(word_list)))] + word_list[int(r.uniform(0,len(word_list)))] + word_list[int(r.uniform(0,len(word_list)))]
    return password


# Now we test the function
print(generate_password())

## #####################

## Factorials (6!) with while loop
# number to find the factorial of
number = 6

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

# write your while loop here
while current <= number:
    # multiply the product so far by the current number
    product = current*product

    # increment current with each iteration until it reaches number
    current += 1

# print the factorial of number
print(product)

## #####################

## Factorial with a for loop
# number to find the factorial of
number = 6

# start with our product equal to one
product = 1

# write your for loop here
for i in range(1, number+1):
    product = product*i

##
## in the Udacity solution they did:
## for num in range(2, number + 1): ...
## this seems weird
##

# print the factorial of number
print(product)

## #####################

## Count by - number counter
start_num = 3 #provide some start number
end_num = 96 #provide some end number that you stop when you hit
count_by = 4 #provide some number to count by

break_num = start_num
# write a while loop that uses break_num as the ongoing number to
#   check against end_num
while break_num <= end_num:
    break_num += count_by

print(break_num)

## #####################

## Quiz: Break number with logic check
start_num = 103 #provide some start number
end_num = 96 #provide some end number that you stop when you hit
count_by = 4 #provide some number to count by

iterations = 0

result = start_num

if end_num < start_num:
    print("Oops! Looks like your start value is greater than the end value. Please try again. \n")
else:
    while result <= end_num:
        result += count_by
        iterations += 1

print("The break number is {} and it was reached after {} iterations.".format(result, iterations))

## #####################

## Quiz: find the nearest square
limit = 40

i = 1

# write your while loop here
while i*i <= limit:
    nearest_square = i*i
    i += 1

print(nearest_square)

## #####################

## You need to write a loop that takes the numbers in a
#  given list named num_list.
#  Your code should add up the odd numbers in the list,
#  but only up to the first 5 odd numbers together. If
#  there are more than 5 odd numbers, you should stop at
#  the fifth. If there are fewer than 5 odd numbers, add
#  all of the odd numbers.

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

result = 0
i = 0

for num in num_list:
    if num % 2 == 1 and i < 5:
        result += num
        i += 1

print("The sum of the first {} odd values is {}.".format(i,result))



## #####################

## Quiz: Zip Coordinates

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here
for label, x, y, z in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {} \n".format(label, x, y, z))

for point in points:
    print(point)

## #####################

## Quiz: Zip Lists to a dictionary

cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights)) # replace with your code
print(cast)

## alternatively:
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = {}

for name, height in zip(cast_names, cast_heights):
    temp = {name: height}
    cast.update(temp)
    # cast.append # = {name'Barney': 72, 'Robin': 68} # replace with your code
print(cast)

## and again, alternatively:
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = {}

for name, height in zip(cast_names, cast_heights):
    cast.update({name: height})
print(cast)

## #####################

## Quiz: Unzip Tuples

cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

# define names and heights here

names, heights =zip(*cast)

print(names)
print(heights)

## #####################

## Quiz: Transpose with Zip

# Use zip to transpose data from a 4-by-3 matrix to
# a 3-by-4 matrix. There's actually a cool trick for
# this! Feel free to look at the solutions if you can't
# figure it out.

data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))
print(data_transpose)

## #####################

## Quiz: Enumerate

cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

# write your for loop here
for i, cast_person in enumerate(cast):
    cast[i] = cast_person + ' ' + str(heights[i])

print(cast)

## #####################

## Quiz: Extract Firsst Names
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.lower().split().pop(0) for name in names]
# write your list comprehension here
print(first_names)

## #####################

## Quiz: Multiples of 3

multiples_3 = [i*3 for i in range(1,21)] # write your list comprehension here
print(multiples_3)

## #####################

## Quiz: Filter names by scores

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name, score in scores.items() if score >=65]
print(passed)

## #####################

## Quiz: Generate Messages
# get and process input for a list of names
names = input('Enter a list of names, separated by commas: ').title().split(',')
# get and process input for a list of the number of assignments
assignments = input('Enter a list of assignment counts, separated by commas: ').split(',')
grades = input('Enter grades, separated by commas: ').split(',')  # get and process input for a list of grades

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for a, b, c in zip(names, assignments, grades):
    potential_grade = int(c) + (2*int(b))
    print(message.format(a, b, c, potential_grade))

## #####################

# Create a 5 x 5 ndarray with consecutive integers from 1 to 25 (inclusive).
# Afterwards use Boolean indexing to pick out only the odd numbers in the array

# Create a 5 x 5 ndarray with consecutive integers from 1 to 25 (inclusive).
# X = np.arange(1,26).reshape(5,5)

# print(X)

# # Use Boolean indexing to pick out only the odd numbers in the array
# Y = X[X%2 = 1]

# print(Y)
y = np.arange(1,5)
X = np.ones((4,4), int)
print(X*y)

## #####################

# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
i = 0

# write your loop here
while len(news_ticker) <= 140:
    if len(news_ticker + headlines[i]) > 140:
        # print("break from this loop")
        remaining_char = 140 - len(news_ticker)
        print(remaining_char, " chars long after new headline \n")
        news_ticker += headlines[i][:remaining_char]
        print(len(news_ticker), ": final length of news ticker string \n")
        break
    else:
        news_ticker += headlines[i] + "|"
        print(len(news_ticker), " chars long after new headline \n")
        i += 1

print(news_ticker)


#############################################################################################################################

headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(len(news_ticker), news_ticker)

##############################################################################################################################

# write your function here
def readable_timedelta(days):
    weeks = int(days/7)
    days = days%7
    solution = "{} week(s) and {} day(s).".format(weeks, days)
    return solution

# test your function
print(readable_timedelta(10))

#####################################################################################

def create_cast_list(filename):
    cast_list = []
    with open(filename) as f:
        for line in f:
            element = line.split(',', 1)
            # print(element[0])
            cast_list.append(element[0])
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list

    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)

#####################################################################################

# initiate empty list to hold user input and sum value of zero
user_list = []
list_sum = 0

# seek user input for ten numbers 
for i in range(10):
    
# check to see if number is even and if yes, add to list_sum
# print incorrect value warning  when ValueError exception occurs
    try:
        userInput = int(input("Enter any 2-digit number: "))
        number = userInput
        user_list.append(number)
        if number % 2 == 0:
            list_sum += number
    except ValueError:
        print("Incorrect value. That's not an int!")

print("user_list: {}".format(user_list))
print("The sum of the even numbers in user_list is: {}.".format(list_sum))


#####################################################################################

# '''
# Depending on where an individual is from we need to tax them 
# appropriately.  The states of CA, MN, and 
# NY have taxes of 7.5%, 9.5%, and 8.9% respectively.
# Use this information to take the amount of a purchase and 
# the corresponding state to assure that they are taxed by the right
# amount.
# '''
state = 'CA' #Either CA, MN, or NY
purchase_amount = 100.00 #amount of purchase

# state = state.upper()

if state.upper() == 'CA': #provide conditional for checking state is CA
    tax_amount = .075
    total_cost = round(purchase_amount*(1+tax_amount), 2)
    result = "Since you're from {}, your total cost is ${}.".format(state.upper(), total_cost)

elif state.upper() == 'MN': #provide conditional for checking state is MN
    tax_amount = .095
    total_cost = round(purchase_amount*(1+tax_amount), 2)
    result = "Since you're from {}, your total cost is ${}.".format(state.upper(), total_cost)

elif state.upper() == 'NY': #provide conditional for checking state is NY
    tax_amount = .089
    total_cost = round(purchase_amount*(1+tax_amount), 2)
    result = "Since you're from {}, your total cost is ${}.".format(state.upper(), total_cost)

else:
    result = "please enter a valid state"

print(result)

#######################################################################################
sentence = []
for words in sentence:
    print(words, '\n')

#######################################################################################

# Write a for loop using range() to print out multiples of 5 up to 30 inclusive

for i in range(5, 31, 5):
    print(i)
    print("")

#######################################################################################


#create new list of usernames with the replacements specified

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for person in names:
    usernames.append(person.lower().replace(" ", "_"))

print(usernames)

#######################################################################################

# modifies existing usernames list and replaces the original values with new ones
usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here
for i in range(len(usernames)):
    usernames[i] = usernames[i].replace(' ', '_').lower()

print(usernames)

#######################################################################################

# check to see which strings in the token list are XML tags
# XML tags can be identified because they begin with '<' and end with '>'
tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for i in range(len(tokens)):
    if tokens[i].startswith('<') and tokens[i].endswith('>'):
        count = count + 1

print(count)

#######################################################################################

# HTML code creation with for loop
items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line
print(html_str)

# write your code here
# for i in range(len(items) + 1):
#     html_str = html_str + i + '\n' #html_str.append(i)
for item in items:
    html_str = html_str + "<li>{}</li>\n".format(item)

html_str = html_str + "</ul>"


print(html_str)

#######################################################################################

## Practice Question: Match Flower Name

# Write your code here
def fileread(filename):
    flower_names = {}
    
    with open(filename, 'r') as f:
        for line in f:
            letter = line.split(': ')[0]
            flower = line.split(': ')[1].strip()
            flower_names.update({letter: flower})

    return flower_names

# HINT: create a dictionary from flowers.txt
flower_names = fileread("flowers.txt")
# HINT: create a function to ask for user's first and last name
# print(flower_names)

prompt = input('Enter your first and last name: ')
first_letter = prompt[0]

print('Unique flower name with your first letter: {}'.format(flower_names.get(first_letter)))

#######################################################################################

## Quiz: NumPy

import numpy as np

# create numpy array of letters a-j
letter_array = np.array(['a','b','c','d','e','f','g','h','i','j'])
print("Letter Array: ", letter_array)

# get dtype of array
print(letter_array.dtype)

# get shape of array
print(letter_array.shape)

# get size of array
print(letter_array.size)

########################################

x = np.linspace(1,25, 49)
print(x)

########################################

x = np.random.normal(0, 1, (10))
print(x*100)

########################################

# x = np.zeros((4,4)).arange(2, 33, 2)
x = np.arange(2, 33, 2).reshape(4,4)
print(x)

x = np.linspace(2, 32, 16).reshape(4,4)
print(x)

########################################

# DO NOT CHANGE THE VARIABLE NAMES

# Given a list representing a few planets
planets = ['Earth', 'Saturn', 'Venus', 'Mars', 'Jupiter']

# Given another list representing the distance of each of these planets from the Sun
# The distance from the Sun is in units of 10^6 km
distance_from_sun = [149.6, 1433.5, 108.2, 227.9, 778.6]


# TO DO: Create a Pandas Series "dist_planets" using the lists above, representing the distance of the planet from the Sun.
# Use the `distance_from_sun` as your data, and `planets` as your index.
dist_planets = pd.Series(data = distance_from_sun, index = planets)
print(dist_planets)

# TO DO: Calculate the time (minutes) it takes light from the Sun to reach each planet. 
# You can do this by dividing each planet's distance from the Sun by the speed of light.
# Use the speed of light, c = 18, since light travels 18 x 10^6 km/minute.
time_light = dist_planets/18
print(time_light)

# TO DO: Use Boolean indexing to select only those planets for which sunlight takes less
# than 40 minutes to reach them.
# We'll check your work by printing out these close planets.
close_planets = time_light[time_light < 40]
print(close_planets)

########################################

# Set the precision of our dataframes to one decimal place.
pd.set_option('precision', 1)

# Create a Pandas DataFrame that contains the ratings some users have given to a series of books. 
# The ratings given are in the range from 1 to 5, with 5 being the best score. 
# The names of the books, the corresponding authors, and the ratings of each user are given below:

books = pd.Series(data = ['Great Expectations', 'Of Mice and Men', 'Romeo and Juliet', 'The Time Machine', 'Alice in Wonderland' ])
authors = pd.Series(data = ['Charles Dickens', 'John Steinbeck', 'William Shakespeare', ' H. G. Wells', 'Lewis Carroll' ])

# User ratings are in the order of the book titles mentioned above
# If a user has not rated all books, Pandas will automatically consider the missing values as NaN.
# If a user has mentioned `np.nan` value, then also it means that the user has not yet rated that book.
user_1 = pd.Series(data = [3.2, np.nan ,2.5])
user_2 = pd.Series(data = [5., 1.3, 4.0, 3.8])
user_3 = pd.Series(data = [2.0, 2.3, np.nan, 4])
user_4 = pd.Series(data = [4, 3.5, 4, 5, 4.2])


# Use the data above to create a Pandas DataFrame that has the following column
# labels: 'Author', 'Book Title', 'User 1', 'User 2', 'User 3', 'User 4'. 
# Let Pandas automatically assign numerical row indices to the DataFrame. 

# TO DO: Create a dictionary with the data given above
dat = {'Book Title' : books,
       'Author' : authors,
       'User 1' : user_1,
       'User 2' : user_2,
       'User 3' : user_3,
       'User 4' : user_4}

# TO DO: Create a Pandas DataFrame using the dictionary created above
book_ratings = pd.DataFrame(dat) 

# If you created the dictionary correctly you should have a Pandas DataFrame
# that has column labels: 
# 'Author', 'Book Title', 'User 1', 'User 2', 'User 3', 'User 4' 
# and row indices 0 through 4.

# Now replace all the NaN values in your DataFrame with the average rating in
# each column. Replace the NaN values in place. 
# HINT: Use the `pandas.DataFrame.fillna(value, inplace = True)` function for substituting the NaN values. 
# Write your code below:
book_ratings.fillna(book_ratings.mean(), inplace = True)

########################################

lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    # Implement your generator function here
    count = start
    for element in iterable:
        yield count, element
        count += 1

for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))

########################################

def chunker(iterable, size):
    # Implement function here
    """Yield successive chunks from iterable of length size."""
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]

for chunk in chunker(range(25), 4):
    print(list(chunk))

########################################

# Testing user input for project

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january','february', 'march', 'april', 'may', 'june']
days_of_week = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

print('Hello! Let\'s explore some US bikeshare data! \n')
while True:
    try:
        # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        city = str(input('\nPlease enter a city to explore (Chicago, New York City, or Washington). \n')).lower()
        if city in CITY_DATA:
            print('\nYou are exploring bikeshare data from {}\n'.format(city.title()))
            break
        else:
            print(city.title(), ' is NOT an acceptable city \n')
            continue
    except:
        print('\nError: Please enter either either "Chicago", "New York City", or "Washington" \n')

while True:
    # get user input for month (all, january, february, ... , june)
    try:
        month = str(input('\nPlease enter a month name from January to June to analyze, or enter "all" to include all months.\nData only available for first 6 months of the year (i.e. January - June) \n')).lower()
        if month in months:
            print('\nYou are exploring bikeshare data from {} during {}\n'.format(city.title(), month.title()))
            break
        elif month == 'all':
            print('\nYou are exploring bikeshare data from {} for all months.\n'.format(city.title()))
            break
        else:
            print(month.title(), ' is NOT a valid month. Please check your spelling. \n')
            continue
    except:
        print('\nPlease enter a full month name from January to June, or enter "all" to explore all months.\n')

while True:
    try:
        # get user input for day of week (all, monday, tuesday, ... sunday)
        day = str(input('\nPlease enter a day of the week to analyze, or enter "all" to include all days \n')).lower()
        if day in days_of_week:
            if month == 'all':
                print('\nYou are exploring bikeshare data from {} during all months and on {}\'s\n'.format(city.title(), day.title()))
                break
            elif month != 'all':
                print('\nYou are exploring bikeshare data from {} during {} on {}\'s\n'.format(city.title(), month.title(), day.title()))
                break
        elif day == 'all':
            if month == 'all':
                print('\nYou are exploring bikeshare data from {} during all months and all days of the week\n'.format(city.title()))
                break
            elif month != 'all':
                print('\nYou are exploring bikeshare data from {} during {} on all days of the week\n'.format(city.title(), month.title()))
                break
        else:
            print(day.title(), ' is NOT a valid day of the week. Please check your spelling. \n')
            continue
    except:
        print('\nPlease enter a valid day of the week.\n')

print(city, month, day)

########################################

# ================== Practice Problems for Project ================== #

df = pd.read_csv("chicago.csv")
print(df.head())  # start by viewing the first few rows of the dataset!

print(df.columns)

print(df.describe())
print(df.info())
print(df['Start Station'].value_counts())
# print(df['Start Station'].unique())
print(df['End Station'].value_counts())
# print(df['End Station'].unique())

filename = 'chicago.csv'

## load data file into a dataframe
df = pd.read_csv(filename)

# df = pd.DataFrame(df) # this may not be needed because the read_csv automatically creates a DataFrame?

## convert the Start Time column to datetime
df['Start Time'] = pd.to_datetime(df['Start Time'])
df['End Time'] = pd.to_datetime(df['End Time'])
df = df.rename(columns={'Unnamed: 0': 'id'})
df['hour'] = df['Start Time'].dt.hour
df['month'] = df['Start Time'].dt.month
df['day_of_week'] = df['Start Time'].dt.day_of_week
print(df)


# print(df.describe())
# print(df.info())
# print(df['Start Station'].value_counts())
# print(df['Start Station'].unique())
# print(df['End Station'].value_counts())
# print(df['End Station'].unique())

# print('The value counts for user types are: \n', df['User Type'].value_counts())
# print('Unique user types: \n', df['User Type'].unique())

user_types = df['User Type'].value_counts()
# print(user_types)

# print(df['Start Time'].head())

# print(df.rename(columns={'Unnamed: 0': 'id'}))

common_hour = df.groupby(['hour'])['Start Time'].count().sort_values(ascending=False)

popular_hour = df['hour'].mode()
print(popular_hour)

# print('The most common hour for rides is ', df['hour'].mode(), ':00')

# ########

city_data = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january','february', 'march', 'april', 'may', 'june']
days_of_week = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(city_data[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['month_name'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    df['start & end station'] = 'Start: ' + df['Start Station'] + ' || End: ' + df['End Station']
    # print(df['start & end station'])
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_int = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month_int]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    
    df.rename(columns={ df.columns[0]: 'id'}, inplace = True)
    # print(df)
    return df
    

city = 'new york city'
month = 'all'
day = 'all'

df=load_data(city, month, day)
# print(df[['Start Time', 'End Time', 'Trip Duration']]) #, df['End Time'], df['Trip Duration'])

total_travel_time_sec = np.sum(df['Trip Duration'])
total_travel_time_min = total_travel_time_sec/60
total_travel_time_hour = total_travel_time_min/60
total_travel_time_day = total_travel_time_hour/24
print('Total travel time for all trips is {} days, which represents {} total hours of travel'.format(round(total_travel_time_day, 1), round(total_travel_time_hour, 1)))

avg_travel_time_sec = np.average(df['Trip Duration'])
avg_travel_time_min = round(avg_travel_time_sec/60, 2)
avg_travel_time_hour = round(avg_travel_time_min/60, 2)
print('The average duration of a trip is {} minutes (or {} hours)'.format(avg_travel_time_min, avg_travel_time_hour))

print((df['Trip Duration']/60).describe())

# display the most common month
common_month_num = mode(df['month'])
month_counts = df['month'].value_counts()
common_month = months[common_month_num - 1].title()

if month == 'all':
    print('\nThe most common month based on number of trips was: {} with {} total trips\n'.format(common_month, month_counts[common_month_num]))
elif month != 'all':
    print('\nYour current dataset is only filtered for {}, therefore the most common month has to be {}\n'.format(month.title(), common_month.title()))


# display the most common day of week
common_day_of_week = mode(df['day_of_week'])
day_counts = df['day_of_week'].value_counts()

if day == 'all':
    print('\nThe most common day of the week, based on number of trips, was: {} with {} total trips\n'.format(common_day_of_week, day_counts[common_day_of_week]))
elif day != 'all':
    print('\nYour current dataset is only filtered for {}\'s, therefore the most common month has to be {}\n'.format(day.title(), common_day_of_week.title()))


# display the most common start hour
common_hour = mode(df['hour'])
hour_counts = df['hour'].value_counts()

if common_hour < 12:
    print('\nThe most common hour for travel was {}A.M. with {} total rides\n'.format(common_hour, hour_counts[common_hour]))
elif common_hour == 12:
    print('\nThe most common hour for travel was {} noon with {} total rides\n'.format(common_hour, hour_counts[common_hour]))
else:
    common_hour_pm = common_hour - 12
    print('\nThe most common hour for travel was {} P.M. with {} total rides\n'.format(common_hour_pm, hour_counts[common_hour]))

# print(df.columns)

busiest_station = mode(df['Start Station'])
station_counts = df['Start Station'].value_counts()
print('The most commonly used Start Station was {}, with {} uses.'.format(busiest_station, station_counts[busiest_station]))

busiest_end_station = mode(df['End Station'])
station_end_counts = df['End Station'].value_counts()

print('The most commonly used End Station was {}, with {} uses.'.format(busiest_end_station, station_end_counts[busiest_end_station]))

# print('\nstart station counts:\n', station_counts)
# print('\nend station counts\n', station_end_counts)

most_common_start_end = mode(df['start & end station'])
start_end_station_counts = df['start & end station'].value_counts()

print('The most common combination of start & end stations was {} with {} rides starting and ending at the respective stations'.format(most_common_start_end, start_end_station_counts[most_common_start_end]))


user_type_counts = df['User Type'].value_counts()
percent = '%'
print('\nUser Type breakout by number of rides:')
print(user_type_counts)
print('\nMeaning {}{} of trips came from subscribers'.format(round((user_type_counts[0]/(user_type_counts[0]+user_type_counts[1])*100), 2), percent))

gender_counts = df['Gender'].value_counts()[[0]]
print('\nGender breakout by number of rides:')
print(gender_counts)
print('\nMeaning {}{} of trips came from male riders\n'.format(round((gender_counts[0]/(gender_counts[0]+gender_counts[1])*100), 2), percent))

## Birth year
## Display earliest, most recent, and most common year of birth
print(df['Birth Year'].value_counts())
birth_year = np.array(df['Birth Year'])
most_recent_birth_year = int(df['Birth Year'].max())
earliest_birth_year = int(df['Birth Year'].min())
most_common_birth_year = int(df['Birth Year'].mode()[0])
print(birth_year)
print(most_recent_birth_year)
print(earliest_birth_year)
print(most_common_birth_year)
birth_year_counts = df['Birth Year'].value_counts()

print('\nThe most common birth year for riders in {} is {} with {} rides born in {}\n'.format(city.title(), most_common_birth_year, birth_year_counts[most_common_birth_year], most_common_birth_year ))
print('The earliest birth year of a rider in {} is {} with {} trips from riders born in {}\n'.format(city.title(), earliest_birth_year, birth_year_counts[earliest_birth_year], earliest_birth_year))
print('The most recent birth year of a rider in {} is {} with {} trips from riders born in {}\n'.format(city.title(), most_recent_birth_year, birth_year_counts[most_recent_birth_year], most_recent_birth_year))

print(df.iloc[0,:])