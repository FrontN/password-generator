import random
import string

lettere = list(string.ascii_letters)
numeri = list(string.digits)
simboli = list(string.punctuation)

print("Welcome to the PyPassword Generator!")
NumlettereScelte = int(input("How many letters would you like in your password?"))
NumnumeriScelti = int(input("How many numbers would you like?"))
NumsimboliScelti= int(input("How many symbols would you like?"))

formula = lambda x,y : random.sample(x, y)

somma = formula(lettere, NumlettereScelte) + formula(numeri, NumnumeriScelti) + formula(simboli, NumsimboliScelti)
random.shuffle(somma)
password = "".join(somma)

print(f"Your password is: {password}")