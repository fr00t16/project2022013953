# write by number int dari 0 - 79
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(79):
	value = randint(0,79)
	print(value)