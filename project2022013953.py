# write by number int dari 0 - 204
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(204):
	value = randint(0,204)
	print(value)