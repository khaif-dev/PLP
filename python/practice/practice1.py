# # Lists
# # create list
# fruits = ["mango", "orange","banana"]
# # editable
# fruits[1] = "apple" #replaces orange with apple
# # print(fruits)
# fruits.append("water melon") #adds melon to end of list (one item)
# fruits.extend(["pine apple", "kiwi", "strawberry"]) #adds multiple items to the end of the list
# # print(fruits[1]) #accessible by index
# # print(fruits[:2]) # Print the first two items in the list using slicing notation
# # print(fruits[-1]) # Print the last item in the list using index notation
# # Create a list called breakfast from the string "eggs, fruit, orange juice"
# breakfast = "eggs, fruit, orange juice".split(", ")
# print(breakfast)
# print(len(breakfast))
# print(len(breakfast)==3)

# # Create a new list called `lengths` using a list
# # comprehension that contains the lengths of each
# # string in the `breakfast` list.
# lengths = [len(item) for item in breakfast]
# print(lengths)
# number = [4,3,2,1]
# total = sum(number)
# print(total)
# number_copy = number[:]
# print(number)
# print(number_copy) 
# number.sort()
# print(number)
# my_numbers = input("Enter your list of integers separated by commas:")
# my_list = [int(x.strip())for x in my_numbers.split(',')]
# print(my_list)
# total = sum(my_list)
# print(total)  
# mean = total / len(my_list)
# print(mean)

# user_input = input("Enter a list of integers separated by commas: ")
# my_list = [int(x.strip()) for x in user_input.split(',')]

# print("Your list:", my_list)



# #Tuple
# # Tuples are similar to lists, but they are not editable.
# allows for duplicates
# brands = ("toyota","mazda","BMW", "suzuki")
# # brands.append("VW") #AttributeError: 'tuple' object has no attribute 'append'
# print(brands[1]) #accessible by index
# print(len(brands))
# # Unpack the tuple into three strings and display them
# brand1, brand2, brand3, brand4 = brands
# print(brand1)
# print(brand2)
# print(brand3)
# print(brand4)
# # Create a tuple containing the letters of your name from a string
# my_tuple = tuple("Immaculate")
# print(my_tuple)
# print("m" in my_tuple) #check for m in my tuple
# print(my_tuple[1:]) #exclude index 0
# print(my_tuple[:1]) #include only index 0
# print(my_tuple[0:4]) #imma slice index 0 to 3
# data = ((1, 2), (3, 4))
# print (data)

# index = 1
# for row in data:
#     print(f"Row {index} sum: {sum(row)}")
#     index += 1


# # SETS
# # Set items are unordered, unchangeable, and do not allow duplicate values.
# my_set = {"road", "air", "water", "rail", "road", "air", "water", "rail"}
# print(my_set) #{'water', 'air', 'rail', 'road'} leaves out duplicates and prints in unordered
# set2 = {"true", 1, "false", True, 0 , False}
# print(set2) # 0 and False, 1 and True are the same in sets


# DICTIONARIES
# # A dictionary is a collection of key-value pairs.
# # Each key is unique and maps to a value.
# 9.6 - Store Relationships in Dictionaries
# Solutions to review exercises


# Exercise 
# 1. Create an empty dictionary
my_dict = {}
# 2. Add some key-value pairs to the dictionary
my_dict['Jane'] = '23'
my_dict['John'] = '40'
my_dict['Mary'] = '34'

# 3. Check if item exist in dict; if not, add them
if 'Alice' not in my_dict:
  my_dict['Alice'] = '45'
if 'John' not in my_dict:
  my_dict['John'] = '40'
print(my_dict)
# 4. Display the contents of the dictionary, one pair at a time
for name, age in my_dict.items():
  print(f"I am {name} , {age} years old")
# 5. Remove a key-value pair from the dictionary
del my_dict['Jane']
print(my_dict)
# 6. Create a dictionary by passing a list to dict()
students = dict(
  [('grace',12),
   ('adam',13),
   ('angel',14)
   ]
)  
print(students)

