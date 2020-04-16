import string
from random import *
characters = string.ascii_letters + string.digits + string.punctuation
print("Password length?")
y=input()
password = "".join(choice(characters) for x in range(randint(3,int(y))))
print(password)
