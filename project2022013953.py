# write by number int dari 0 - 624
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(624):
	value = randint(0,624)
	print(value)