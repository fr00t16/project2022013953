# write by number int dari 0 - 397
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(397):
	value = randint(0,397)
	print(value)