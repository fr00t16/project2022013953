# write by number int dari 0 - 63
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(63):
	value = randint(0,63)
	print(value)