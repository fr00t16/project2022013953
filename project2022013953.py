# write by number int dari 0 - 591
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(591):
	value = randint(0,591)
	print(value)