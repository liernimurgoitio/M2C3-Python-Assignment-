#Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.
string_variable = 'This is a M2C3 Python Assignment'
number_variable = 3
list_variable = ['python', 'php', 200, 8.5]
boolean_variable = True

print(string_variable)
print(number_variable)
print(list_variable)
print(boolean_variable)

#Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable.
index = string_variable[0: 3]
print(index)

#Exercise 3: Use an index to grab the first element from your list.
index = list_variable[0]
print(index)

#Exercise 4: Create a new number variable that adds 10 to your original number.
new_number_variable = number_variable+10
print(new_number_variable)

#Exercise 5: Use an index to get the last element in your list.
index = list_variable[-1]
print(index)

#Exercise 6: Use split to transform the following string into a list.
#names = 'harry,alex,susie,jared,gail,conner'
names = 'harry,alex,susie,jared,gail,conner'
list_of_names = names.split(',')
print(list_of_names)

#Exercise 7: Get the first word from your string using indexes. 
# Use the upper function to transform the letters into uppercase. 
# Create a new string that takes the uppercase word and the rest of the original string.
first_word_index = string_variable[0:4]
string_variable_uppercase = first_word_index.upper()
new_string_uppercase_word = string_variable_uppercase + string_variable[4:] 
print(first_word_index)
print(string_variable_uppercase)
print(new_string_uppercase_word)

#Exercise 8: Use string interpolation to print out a sentence that contains your number variable.
print(f'The {number_variable} top up')

#Exercise 9: Print “hello world”.
print('hello world')