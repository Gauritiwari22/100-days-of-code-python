#Project5
print("Welcome to the PyPassword Generator!")

user_letters=int(input("How many letters would you like to keep in your password?\n"))
user_symbols=int(input("How many symbols would you like in your password?\n"))
user_numbers=int(input("How many numbers would you like in your password?\n"))

import string
letters=list(string.ascii_letters)
symbols=list(string.punctuation)
numbers=list(string.digits)

import random
choice1=random.choices(letters,k=user_letters)
choice2=random.choices(symbols,k=user_symbols)
choice3=random.choices(numbers,k=user_numbers)

final_list=choice1+choice2+choice3
print(final_list)

password=""
random.shuffle(final_list)
for i in final_list:
    password+=i

print("Your password is:",password)