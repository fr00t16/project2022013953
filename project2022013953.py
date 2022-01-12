# write by number int dari 0 - 164
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(164):
	value = randint(0,164)
	print(value)