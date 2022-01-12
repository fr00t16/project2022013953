# write by number int dari 0 - 628
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(628):
	value = randint(0,628)
	print(value)