# write by number int dari 0 - 303
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(303):
	value = randint(0,303)
	print(value)