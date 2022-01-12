# write by number int dari 0 - 693
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(693):
	value = randint(0,693)
	print(value)