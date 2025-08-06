# Write a program that accepts user input to create a list of integers. 
# Then, compute the sum of all the integers in the list
user_number = input("Enter a list of integers separated by commas (1,2,3...):")
user_list = [int(x.strip()) for x in user_number.split(',')]
sum_of_num = sum(user_list)
print(f"The sum of your number = {sum_of_num}")

# Create a tuple containing the names of five of your favorite books. 
# Then, use a for loop to print each book name on a separate line.
books = ("THE EXECUTIONER", "HOME GOING","DAMU NYEUSI","KIFO KISIMANI")
for book in books:  
  print(book)

# Write a program that uses a dictionary to store information about a person, 
# such as their name, age, and favorite color. 
# Ask the user for input and store the information in the dictionary. 
# Then, print the dictionary to the console.
dict_users = {}
dict_users['name'] = input("Enter your name: ")
dict_users['age'] = int(input("Enter your age: "))
dict_users['favorite_color'] = input("Enter your favorite color: ")
print(dict_users)

user_set1 = input("Enter your first set of integers separated by commas:")
user_set2 = input("Enter your second set of integers separated by commas:")
# split(',') splits the string into a list of strings.
# map(int, ...) converts each string into an integer.
# set(int, ...) can’t convert a whole list, only one value at a time therefore wont work here.
# set(...) converts the list into a set.
set1 = set(map(int,user_set1.strip().split(',')))
print(set1)
set2 = set(map(int,user_set2.strip().split(',')))
print(set2)
final_set = set1.union(set2) #joins set one to set 2
print(final_set)
final_set = set1.intersection(set2) #only takes the common elements
print(final_set)
final_set = set1.difference(set2) #only takes the elements unique to set 1
print(final_set)
final_set = set2.difference(set1) #only takes the elements unique to set 1
print(final_set)
final_set = set1.symmetric_difference(set2) #takes the elements that are not common in
print(final_set)


# Create a program that stores a list of words. 
# Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.
my_words = ["tyler", "lifted", "his", "right", "index", "finger", "asking", "for",
             "a","minute", "he", "then", "searched", "through", "the", "rest", "of", "the",""
             "photos", "until", "he", "found", "the", "one", "he", "was", "looking", "for"
            ]
odd_length_words = []
for word in my_words:
  if len(word) % 2 == 0:
    odd_length_words.append(word)
print(odd_length_words)