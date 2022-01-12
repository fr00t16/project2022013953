# write by number int dari 0 - 262
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(262):
	value = randint(0,262)
	print(value)