# Write a program to generate a random number. Raise a user-defined exception if the number is below 0.5.

import random
class randomError(Exception):
    def _init_(self,arg):
        self.msg=arg
try:
    number=random.random()
    if number<0.5:
        raise randomError("Random error is generated")
    print("Random number generated",number)
except randomError as e:
    print(e)
else:
    print("No exception")
finally:
    print("Bye")
