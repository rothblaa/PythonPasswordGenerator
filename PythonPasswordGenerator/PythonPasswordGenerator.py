#importing random allows for use of random method 
import random

#numbers, letters, and symbols to be used for the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#welcome message to the app
print("Welcome to the PyPassword Generator!")

#inputs saved into variables to be able to iterate over the code
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#set up a list vs. a string so you can randomize the chars
password_list = []

#iterate over the  letters list
for char in range(0, nr_letters):
    #1 - 4
    password_list += random.choice(letters)

#iterate over the symbols list
for char in range(0, nr_symbols):
    password_list += random.choice(symbols)

#iterate over the numbers list
for char in range(0, nr_numbers):
    password_list += random.choice(numbers)

#print the selected characters, shuffle the characters, print the shuffled characters
print(f"Your password characters are: {password_list}")
random.shuffle(password_list)
print(f"Your jumbled password characters are: {password_list}")

#turn the characters in the list back into a string
password = ""
for char in password_list:
    password += char

#print the string
print(f"Your final password is: {password}")








