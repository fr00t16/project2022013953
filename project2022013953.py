# write by number int dari 0 - 49
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(49):
	value = randint(0,49)
	print(value)