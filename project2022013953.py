# write by number int dari 0 - 32
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(32):
	value = randint(0,32)
	print(value)