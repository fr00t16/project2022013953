# write by number int dari 0 - 543
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(543):
	value = randint(0,543)
	print(value)