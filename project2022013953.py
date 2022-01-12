# write by number int dari 0 - 513
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(513):
	value = randint(0,513)
	print(value)