#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
ran_letters= random.sample(letters, nr_letters)
ran_symbols= random.sample(symbols, nr_symbols)
ran_numbers= random.sample(numbers, nr_numbers)
ran_password= ran_letters+ran_numbers+ran_symbols
final_password= "".join(str(item) for item in ran_password)

print(final_password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
ran_letters= random.sample(letters, nr_letters)
ran_symbols= random.sample(symbols, nr_symbols)
ran_numbers= random.sample(numbers, nr_numbers)
ran_password= ran_letters+ran_numbers+ran_symbols
random.shuffle(ran_password)

final_password= "".join(str(item) for item in ran_password)

print(final_password)