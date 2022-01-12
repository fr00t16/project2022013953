# write by number int dari 0 - 91
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(91):
	value = randint(0,91)
	print(value)