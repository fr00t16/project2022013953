# write by number int dari 0 - 309
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(309):
	value = randint(0,309)
	print(value)