# write by number int dari 0 - 626
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(626):
	value = randint(0,626)
	print(value)